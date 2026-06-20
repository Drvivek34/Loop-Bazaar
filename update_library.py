import json
import os
import re
import subprocess
import urllib.request
from datetime import datetime

# Configurations
DB_PATH = "/root/github-loop-library/loops_data.json"
REPO_DIR = "/root/github-loop-library"
CATALOG_URL = "https://signals.forwardfuture.ai/loop-library/catalog.json"

def run_cmd(cmd, cwd=REPO_DIR):
    """Helper to run a shell command and return output."""
    try:
        res = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
        return res.stdout.strip(), res.stderr.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command '{cmd}' failed with exit code {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise e

def scrape_latest_loops(db_data):
    """Scrapes the latest loops from the official catalog URL."""
    print("Scraping latest loops from Forward Future...")
    try:
        req = urllib.request.Request(CATALOG_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req) as response:
            external_data = json.loads(response.read().decode('utf-8'))
        
        existing_slugs = {loop["slug"] for loop in db_data.get("loops", [])}
        new_loops_count = 0

        for ext_loop in external_data.get("loops", []):
            slug = ext_loop["slug"]
            if slug not in existing_slugs:
                print(f"Found new loop online: {ext_loop['title']}")
                # Add default reviews structure for new loops
                ext_loop["reviews"] = []
                ext_loop["averageRating"] = 5.0  # Seed with a clean rating
                db_data["loops"].append(ext_loop)
                existing_slugs.add(slug)
                new_loops_count += 1
        
        print(f"Finished scraping. Added {new_loops_count} new loops.")
        return new_loops_count
    except Exception as e:
        print(f"Error scraping latest loops: {e}")
        return 0

def process_github_pull_requests():
    """Checks for open pull requests, runs tests, and merges them if passing."""
    print("Checking for open GitHub Pull Requests...")
    try:
        # Check if gh CLI is available and authenticated
        run_cmd("gh auth status")
    except Exception:
        print("GitHub CLI not authenticated or not installed. Skipping PR processing.")
        return

    try:
        # Get list of open PRs
        pr_list_out, _ = run_cmd("gh pr list --state open --json number,title,headRefName")
        if not pr_list_out:
            print("No open PRs found.")
            return
        
        prs = json.loads(pr_list_out)
        print(f"Found {len(prs)} open Pull Requests.")

        for pr in prs:
            pr_num = pr["number"]
            pr_title = pr["title"]
            pr_branch = pr["headRefName"]
            
            print(f"Processing PR #{pr_num}: '{pr_title}' on branch '{pr_branch}'")
            
            try:
                # Checkout PR branch
                run_cmd(f"gh pr checkout {pr_num}")
                
                # Run unit tests
                print("Running test suite on PR branch...")
                run_cmd("python3 -m unittest /root/github-loop-library/test_library.py")
                
                # If tests pass, merge the PR
                print(f"Tests passed! Merging PR #{pr_num}...")
                run_cmd(f"gh pr merge {pr_num} --merge --delete-branch -y")
                print(f"Successfully merged PR #{pr_num}.")
            except Exception as e:
                print(f"PR #{pr_num} failed verification: {e}")
                # Leave a feedback comment on the PR
                try:
                    comment = "Automated check: Unit tests failed on this branch. Please check database formatting and integrity before re-submitting."
                    run_cmd(f"gh pr comment {pr_num} -b '{comment}'")
                except Exception as comment_err:
                    print(f"Failed to post comment on PR #{pr_num}: {comment_err}")
            finally:
                # Always return to main branch
                run_cmd("git checkout main")
                run_cmd("git pull origin main || true")
    except Exception as e:
        print(f"Error processing Pull Requests: {e}")

def parse_feedback_issue(body):
    """Parses rating, comment, loop slug, and author from feedback issue body."""
    loop_slug = None
    rating = None
    author = "Anonymous"
    comment = "No comment"

    # Search for Loop slug: matches "- **Loop**: Title (slug)"
    loop_match = re.search(r"-\s*\*\*Loop\*\*:\s*.*?\s*\((.*?)\)", body, re.IGNORECASE)
    if loop_match:
        loop_slug = loop_match.group(1).strip()
    else:
        # Fallback to look for titles like Feedback: [slug]
        pass

    # Search for Rating: matches "- **Rating**: 5/5 Stars" or "- **Rating**: 5"
    rating_match = re.search(r"-\s*\*\*Rating\*\*:\s*(\d+)", body, re.IGNORECASE)
    if rating_match:
        rating = int(rating_match.group(1).strip())

    # Search for Author: matches "- **Author**: Name"
    author_match = re.search(r"-\s*\*\*Author\*\*:\s*(.*)", body, re.IGNORECASE)
    if author_match:
        author = author_match.group(1).strip()

    # Search for Feedback comment: matches "- **Feedback**: Comment"
    comment_match = re.search(r"-\s*\*\*Feedback\*\*:\s*(.*)", body, re.IGNORECASE)
    if comment_match:
        comment = comment_match.group(1).strip()

    return loop_slug, rating, author, comment

def parse_submission_issue(body):
    """Parses new loop details from submission issue body."""
    title = None
    category = "engineering"
    author = "Anonymous"
    description = ""
    verification = ""
    prompt = ""
    steps = []

    # Simple regex parsing
    title_match = re.search(r"-\s*\*\*Title\*\*:\s*(.*)", body, re.IGNORECASE)
    if title_match: title = title_match.group(1).strip()

    category_match = re.search(r"-\s*\*\*Category\*\*:\s*(.*)", body, re.IGNORECASE)
    if category_match: category = category_match.group(1).strip().lower()

    author_match = re.search(r"-\s*\*\*Author\*\*:\s*(.*)", body, re.IGNORECASE)
    if author_match: author = author_match.group(1).strip()

    desc_match = re.search(r"-\s*\*\*Description\*\*:\s*(.*)", body, re.IGNORECASE)
    if desc_match: description = desc_match.group(1).strip()

    ver_match = re.search(r"-\s*\*\*Verification\*\*:\s*(.*)", body, re.IGNORECASE)
    if ver_match: verification = ver_match.group(1).strip()

    # Prompt block search
    prompt_match = re.search(r"### Prompt / Instructions\s*```.*?\n([\s\S]*?)```", body, re.IGNORECASE)
    if prompt_match: prompt = prompt_match.group(1).strip()

    # Steps list search
    steps_section = re.search(r"### Implementation Steps\n([\s\S]*?)(?:$|##)", body, re.IGNORECASE)
    if steps_section:
        steps_text = steps_section.group(1)
        steps = [line.replace("-", "").strip() for line in steps_text.split("\n") if line.strip().startswith("-")]

    return {
        "title": title,
        "category": category,
        "author": author,
        "description": description,
        "verification": verification,
        "prompt": prompt,
        "steps": steps
    }

def process_github_issues(db_data):
    """Processes open GitHub Issues for loop submissions, feedback reviews, and general maintenance."""
    print("Checking for open GitHub Issues...")
    try:
        run_cmd("gh auth status")
    except Exception:
        print("GitHub CLI not authenticated or not installed. Skipping issues processing.")
        return 0

    issues_processed = 0
    try:
        # Get open issues
        issue_list_out, _ = run_cmd("gh issue list --state open --json number,title,body,labels")
        if not issue_list_out:
            print("No open issues found.")
            return 0
        
        issues = json.loads(issue_list_out)
        print(f"Found {len(issues)} open Issues.")

        for issue in issues:
            issue_num = issue["number"]
            issue_title = issue["title"]
            issue_body = issue["body"]
            labels = [l["name"] for l in issue.get("labels", [])]

            # Check if feedback issue
            if "feedback" in labels or issue_title.startswith("Feedback:"):
                print(f"Processing Feedback Issue #{issue_num}...")
                slug, rating, author, comment = parse_feedback_issue(issue_body)
                
                # Check fallback slug if parsing failed
                if not slug and ":" in issue_title:
                    slug = issue_title.split(":")[-1].strip()

                if slug and rating:
                    # Find loop in database
                    loop_found = False
                    for loop in db_data.get("loops", []):
                        if loop["slug"] == slug:
                            loop["reviews"].append({
                                "author": author,
                                "rating": rating,
                                "comment": comment,
                                "date": datetime.today().strftime('%Y-%m-%d')
                            })
                            # Re-calculate rating
                            total = sum(r["rating"] for r in loop["reviews"])
                            loop["averageRating"] = round(total / len(loop["reviews"]), 1)
                            loop_found = True
                            break
                    
                    if loop_found:
                        print(f"Appended rating {rating}* to loop '{slug}' successfully.")
                        run_cmd(f"gh issue close {issue_num} -c 'Automated Check: Rating & comment integrated successfully into database.'")
                        issues_processed += 1
                    else:
                        print(f"Loop slug '{slug}' not found in database. Leaving issue open.")
                else:
                    print(f"Could not parse rating/slug from issue #{issue_num}.")

            # Check if loop submission issue
            elif "submission" in labels or issue_title.startswith("Submission:"):
                print(f"Processing Loop Submission Issue #{issue_num}...")
                sub = parse_submission_issue(issue_body)
                
                if sub["title"] and sub["prompt"] and len(sub["steps"]) > 0:
                    slug = sub["title"].lower().replace(" ", "-")
                    slug = re.sub(r'[^a-z0-9\-]', '', slug)
                    
                    # Generate number by finding max number
                    numbers = []
                    for l in db_data.get("loops", []):
                        try:
                            numbers.append(int(l["number"]))
                        except ValueError:
                            pass
                    next_number_str = str(max(numbers) + 1).zfill(3) if numbers else "001"

                    new_loop = {
                        "number": next_number_str,
                        "slug": slug,
                        "title": sub["title"],
                        "url": "#",
                        "category": {
                            "slug": sub["category"],
                            "label": sub["category"].capitalize()
                        },
                        "author": sub["author"],
                        "published": datetime.today().strftime('%Y-%m-%d'),
                        "modified": datetime.today().strftime('%Y-%m-%d'),
                        "description": sub["description"],
                        "useWhen": sub["description"],
                        "prompt": sub["prompt"],
                        "verification": {
                            "title": sub["verification"],
                            "detail": "Verified by submission script."
                        },
                        "steps": sub["steps"],
                        "why": "Community contributed loop.",
                        "implementationNote": "Verify functionality locally.",
                        "keywords": [sub["category"], "community-contribution"],
                        "reviews": [],
                        "averageRating": 5.0
                    }

                    db_data["loops"].append(new_loop)
                    print(f"Added new loop '{sub['title']}' with slug '{slug}' successfully.")
                    run_cmd(f"gh issue close {issue_num} -c 'Automated Check: Loop parsed and added to library database. Thank you!'")
                    issues_processed += 1
                else:
                    print(f"Could not parse loop details from issue #{issue_num}. Missing title, prompt, or steps.")

            # General issue: Try to implement using LLM if api key is available
            else:
                api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
                if api_key:
                    print(f"Attempting to autonomously implement fix for Issue #{issue_num} using Gemini API...")
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=api_key)
                        
                        # Fetch project files contents
                        files_to_read = ["index.html", "style.css", "script.js", "loops_data.json"]
                        project_context = ""
                        for filename in files_to_read:
                            filepath = os.path.join(REPO_DIR, filename)
                            if os.path.exists(filepath):
                                with open(filepath, "r", encoding="utf-8") as pf:
                                    project_context += f"--- FILE: {filename} ---\n{pf.read()}\n\n"
                        
                        model = genai.GenerativeModel('gemini-2.5-flash')
                        prompt = (
                            f"You are an expert web development agent. Your task is to resolve a GitHub issue.\n"
                            f"Issue Title: {issue_title}\n"
                            f"Issue Body: {issue_body}\n\n"
                            f"Here is the project files context:\n{project_context}\n\n"
                            f"Analyze the issue and rewrite the single file that needs changes. Output ONLY the complete "
                            f"revised code block for the file, prefixing the block with the tag 'REVISED_FILE: <filename>' "
                            f"so it can be easily written to disk. If no files need modifications, output 'NO_CHANGES_NEEDED'."
                        )
                        
                        response = model.generate_content(prompt)
                        resp_text = response.text.strip()
                        
                        if "REVISED_FILE:" in resp_text:
                            # Parse file to overwrite
                            lines = resp_text.split("\n")
                            first_line = lines[0]
                            match = re.search(r"REVISED_FILE:\s*(\S+)", first_line)
                            if match:
                                target_file = match.group(1)
                                # Extract code block content
                                code_content = "\n".join(lines[1:])
                                # Strip markdown code block wrappers
                                code_content = re.sub(r"^```[a-zA-Z0-9]*\n", "", code_content)
                                code_content = re.sub(r"\n```$", "", code_content)
                                
                                target_path = os.path.join(REPO_DIR, target_file)
                                print(f"Rewriting target file: {target_path}")
                                
                                # Backup original
                                with open(target_path, "r", encoding="utf-8") as orig:
                                    orig_content = orig.read()
                                
                                # Write new content
                                with open(target_path, "w", encoding="utf-8") as out_f:
                                    out_f.write(code_content)
                                
                                # Verify using tests
                                try:
                                    run_cmd("python3 -m unittest /root/github-loop-library/test_library.py")
                                    print("Autocoded fix passes unit tests! Committing changes...")
                                    run_cmd(f"git add {target_file}")
                                    run_cmd(f"git commit -m 'Auto-implemented fix for Issue #{issue_num}'")
                                    run_cmd(f"gh issue close {issue_num} -c 'Automated Check: Issue resolved and fix deployed autonomously by agent schedule script.'")
                                    issues_processed += 1
                                except Exception as test_err:
                                    print(f"Auto-coded fix failed tests: {test_err}. Rolling back changes.")
                                    with open(target_path, "w", encoding="utf-8") as rollback_f:
                                        rollback_f.write(orig_content)
                        else:
                            print("Gemini response did not request file changes or returned NO_CHANGES_NEEDED.")
                    except Exception as llm_err:
                        print(f"LLM auto-implementation failed: {llm_err}")
                else:
                    print(f"Issue #{issue_num} is a general issue, but no Gemini API key was found in the environment. Leaving open.")
                    
    except Exception as e:
        print(f"Error processing GitHub Issues: {e}")
    
    return issues_processed

def main():
    print(f"Running Loop Library automation script at {datetime.now().isoformat()}")
    
    # 1. Load database
    if not os.path.exists(DB_PATH):
        print(f"Database path {DB_PATH} not found.")
        return

    with open(DB_PATH, "r", encoding="utf-8") as f:
        db_data = json.load(f)

    # 2. Scrape external loops
    scraped_count = scrape_latest_loops(db_data)
    
    # 3. Pull Requests Processing
    process_github_pull_requests()

    # 4. GitHub Issues Processing
    issues_processed_count = process_github_issues(db_data)

    # 5. Save updated database if any modifications were made
    if scraped_count > 0 or issues_processed_count > 0:
        db_data["updated"] = datetime.today().strftime('%Y-%m-%d')
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(db_data, f, indent=2)
        print("Updated database saved successfully.")

        # 6. Commit and Push back to GitHub
        try:
            run_cmd("git add loops_data.json")
            run_cmd('git commit -m "Automated daily loop catalog & rankings update [skip ci]"')
            run_cmd("git push origin main")
            print("Successfully pushed updates to GitHub repository.")
        except Exception as git_err:
            print(f"Error committing/pushing database changes: {git_err}")
    else:
        print("No changes were made to the database. Skipping Git push.")

if __name__ == "__main__":
    main()
