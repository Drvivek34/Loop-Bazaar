import json
import os

DB_PATH = "/root/Loop-Bazaar/loops_data.json"
REPO_DIR = "/root/Loop-Bazaar"

def compile_markdown():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    loops = data.get("loops", [])
    updated_date = data.get("updated", "2026-06-20")
    total_count = data.get("loopCount", len(loops))
    categories = data.get("categories", [])

    print("Compiling root README.md...")
    
    # 1. Start root README content
    readme = []
    readme.append("# 🌟 Loop-Bazaar: The Curated AI Agent Loops Directory")
    readme.append("\n![Loop-Bazaar Banner](assets/banner.jpg)")
    readme.append(f"\nWelcome to **Loop-Bazaar**! A premium, comprehensive bazaar of **{total_count}** repeatable AI agent workflows, design patterns, and instructions with specific verification checkpoints and community ratings. All loops are organized into category folders with individual details pages.")
    readme.append(f"\n*Last updated: {updated_date} | Version: 1.0.0 | Daily updates at 6:00 AM IST*")
    
    # Add supported platforms section
    readme.append("\n## 🔌 Supported Platforms & Agentic Rigs")
    readme.append("The workflows and prompts in Loop-Bazaar are designed to be environment-agnostic and can be implemented in a wide range of platforms:")
    readme.append("- 🤖 **Claude Code (Developer Preview)**: Execute iterative code sweeps, PR testing, and test suites directly using the CLI plugin models (`clodex`, `autonomy-loop`).")
    readme.append("- 🦅 **Google Antigravity (AGY)**: Pair program, write/verify tests, and trigger daily cron updates automatically using the AGY Agent and SDK.")
    readme.append("- 🛠️ **Aider / Cursor / Windsurf**: Run interactive file edit-and-run loops, passing compiler errors back to the model until verify stages clear.")
    readme.append("- 🕸️ **LangGraph (LangChain)**: Orchestrate stateful multi-agent systems with explicit conditional edges mapping to loop stopping conditions.")
    readme.append("- 👥 **CrewAI / Microsoft AutoGen**: Define worker agents (e.g. Researcher, Reviewer) and set collaborative loops where output passes between work folders.")
    readme.append("- 🚀 **GitHub Actions / CI Pipelines**: Run reliability sweeps (like the docs sweep or production log checks) on a scheduled runner or commit hook.")

    # How to add new loops section
    readme.append("\n## 🤝 How to Add New Loops on GitHub First")
    readme.append("We welcome community additions! You can contribute in two ways:")
    readme.append("\n### Option A: Create a GitHub Issue (No coding required)")
    readme.append("1. Go to the **Issues** tab on our [GitHub Repository](https://github.com/Drvivek34/Loop-Bazaar).")
    readme.append("2. Click **New Issue** and choose the **Loop Submission Template** (or create a general issue with label `submission`).")
    readme.append("3. Fill in the details (Title, Category, Prompt, Steps, and Verification stopping condition).")
    readme.append("4. Click submit. Our daily automation script running at 6:00 AM will automatically parse the issue, format it, add it to the directory, and compile the updated markdown files!")
    readme.append("\n### Option B: Create a Pull Request (PR)")
    readme.append("1. Fork this repository.")
    readme.append("2. Open the database file [loops_data.json](loops_data.json) and add your new loop object to the `loops` array. Ensure you increment the number index.")
    readme.append("3. Commit and open a Pull Request. Our daily cron job will checkout your branch, run the test suite [test_library.py](test_library.py) to check schema validity, and automatically merge the PR if it passes!")

    readme.append("\n## 📚 Directory Index (Master Loops Table)")
    readme.append("Click on the titles to view complete details (Prompts, Steps, and Why it works) inside their respective category files.")
    readme.append("\n| ID | Category | Title | Author | Rating | Notes / Use Cases |")
    readme.append("|---|---|---|---|---|---|")

    # Group loops by category for folder structure
    cat_loops = {cat["slug"]: [] for cat in categories}

    # Sort loops for index table by rating (highest first), then reviews volume
    sorted_loops = sorted(loops, key=lambda l: (l.get("averageRating", 0), len(l.get("reviews", []))), reverse=True)

    for loop in sorted_loops:
        num = loop.get("number", "0000")
        slug = loop.get("slug", "unknown")
        title = loop.get("title", "Unknown Loop")
        author = loop.get("author", "Anonymous")
        rating = loop.get("averageRating", 5.0)
        desc = loop.get("description", "")
        cat_slug = loop["category"]["slug"]
        cat_label = loop["category"]["label"]
        
        # Link to the standalone file in the category directory
        link = f"{cat_slug}/{slug}.md"
        stars = "★" * int(rating) + "☆" * (5 - int(rating))
        readme.append(f"| #{num} | {cat_label} | [{title}]({link}) | {author} | {stars} {rating} | {desc} |")
        
        # Add to category grouping
        cat_loops[cat_slug].append(loop)

    # Write root README.md
    with open(os.path.join(REPO_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print("Root README.md compiled successfully.")

    # 2. Compile Folders, Category Master READMEs, and Smaller Loop Files
    for cat in categories:
        cat_slug = cat["slug"]
        cat_label = cat["label"]
        list_of_loops = cat_loops[cat_slug]
        
        # Create category folder
        cat_dir = os.path.join(REPO_DIR, cat_slug)
        os.makedirs(cat_dir, exist_ok=True)
        
        # Build category master loop file (category/README.md)
        print(f"Compiling category master file {cat_slug}/README.md...")
        cat_readme = []
        cat_readme.append(f"# 🛠️ {cat_label} Loops - Loop-Bazaar")
        cat_readme.append(f"\nWelcome to the **{cat_label}** category folder! This folder contains {len(list_of_loops)} loops.")
        cat_readme.append("\n[← Back to Global Directory Index](../README.md)")
        cat_readme.append("\n## Category Index Table")
        cat_readme.append("\n| ID | Title | Author | Rating | Notes / Use Cases |")
        cat_readme.append("|---|---|---|---|---|")
        
        # Sort category loops chronologically by loop number
        sorted_cat_loops = sorted(list_of_loops, key=lambda l: l.get("number", "0000"))
        
        for loop in sorted_cat_loops:
            num = loop.get("number", "0000")
            slug = loop.get("slug", "unknown")
            title = loop.get("title", "Unknown Loop")
            author = loop.get("author", "Anonymous")
            rating = loop.get("averageRating", 5.0)
            desc = loop.get("description", "")
            
            # Category index table links to the smaller loop file
            link_to_smaller = f"{slug}.md"
            stars = "★" * int(rating) + "☆" * (5 - int(rating))
            cat_readme.append(f"| #{num} | [{title}]({link_to_smaller}) | {author} | {stars} {rating} | {desc} |")
            
            # Generate the smaller detailed file for the individual loop
            compile_smaller_loop_file(loop, cat_dir, cat_label)

        # Write category README.md
        with open(os.path.join(cat_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(cat_readme))
        
        print(f"Category master {cat_slug}/README.md compiled successfully.")

def compile_smaller_loop_file(loop, cat_dir, cat_label):
    """Compiles a standalone markdown file for a single loop."""
    slug = loop.get("slug", "unknown")
    title = loop.get("title", "Unknown Loop")
    num = loop.get("number", "0000")
    author = loop.get("author", "Anonymous")
    rating = loop.get("averageRating", 5.0)
    desc = loop.get("description", "")
    use_when = loop.get("useWhen", "")
    prompt = loop.get("prompt", "")
    ver_title = loop["verification"]["title"]
    ver_detail = loop["verification"]["detail"]
    why = loop.get("why", "")
    note = loop.get("implementationNote", "")
    keywords = ", ".join(loop.get("keywords", []))
    
    loop_md = []
    loop_md.append(f"# {title}")
    loop_md.append(f"\n**Loop ID**: #{num} | **Category**: {cat_label} | **Author**: {author} | **Rating**: ⭐ {rating}/5.0")
    loop_md.append("\n[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)")
    loop_md.append("\n---")
    
    loop_md.append(f"\n## 📝 Description")
    loop_md.append(desc)
    
    loop_md.append(f"\n## 🎯 Use Case (When to Use)")
    loop_md.append(f"> {use_when}")
    
    loop_md.append(f"\n## ⚡ System Prompt / Instructions")
    loop_md.append("```")
    loop_md.append(prompt)
    loop_md.append("```")
    
    loop_md.append(f"\n## 🏁 Implementation Steps")
    for idx, step in enumerate(loop["steps"]):
        loop_md.append(f"{idx + 1}. {step}")
    
    loop_md.append(f"\n## 🛑 Stopping Condition (Verification)")
    loop_md.append(f"**Verification Check**: {ver_title}")
    loop_md.append(f"- *Detail*: {ver_detail}")
    
    loop_md.append(f"\n## 💡 Why it works")
    loop_md.append(why)
    
    if note:
        loop_md.append(f"\n## ⚠️ Implementation Note")
        loop_md.append(f"* {note}")

    loop_md.append(f"\n## 🏷️ Keywords")
    loop_md.append(keywords)

    # Reviews
    loop_md.append(f"\n## 💬 Reviews & Feedback")
    reviews = loop.get("reviews", [])
    if reviews:
        for r in reviews:
            stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
            loop_md.append(f"- **{r['author']}** ({stars} {r['rating']}/5): *{r['comment']}* ({r['date']})")
    else:
        loop_md.append("- *No reviews yet.*")

    # Write smaller file
    file_path = os.path.join(cat_dir, f"{slug}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(loop_md))

if __name__ == "__main__":
    compile_markdown()
