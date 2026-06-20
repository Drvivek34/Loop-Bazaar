import json
import os

DB_PATH = "/root/github-loop-library/loops_data.json"
REPO_DIR = "/root/github-loop-library"
CATEGORIES_DIR = os.path.join(REPO_DIR, "categories")

# HTML-safe slugifier helper
def make_html_anchor(slug):
    return slug

def compile_markdown():
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found.")
        return

    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    loops = data.get("loops", [])
    updated_date = data.get("updated", "2026-06-20")
    total_count = data.get("loopCount", len(loops))

    # Create categories folder if it doesn't exist
    os.makedirs(CATEGORIES_DIR, exist_ok=True)

    print("Compiling root README.md...")
    
    # 1. Start README content
    readme = []
    readme.append("# 🌟 Loop-Bazaar: The Curated AI Agent Loops Directory")
    readme.append(f"\nWelcome to **Loop-Bazaar**! A premium, comprehensive bazaar of **{total_count}** repeatable AI agent workflows, design patterns, and instructions with specific verification checkpoints and community ratings. All loops are visible directly in this file, sorted by default by rating.")
    readme.append(f"\n*Last updated: {updated_date} | Version: 1.0.0 | Daily updates at 6:00 AM IST*")
    
    readme.append("\n## 🤝 How to Add New Loops on GitHub First")
    readme.append("We welcome community additions! You can contribute in two ways:")
    readme.append("\n### Option A: Create a GitHub Issue (No coding required)")
    readme.append("1. Go to the **Issues** tab on our [GitHub Repository](https://github.com/Drvivek34/github-loop-library).")
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

    # Group loops by category for category-specific files
    cat_loops = {
        "engineering": [],
        "evaluation": [],
        "operations": [],
        "content": [],
        "design": []
    }

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
        
        # Add to master table
        # We link to the specific anchor inside the category file
        link = f"categories/{cat_slug}.md#{slug}"
        stars = "★" * int(rating) + "☆" * (5 - int(rating))
        readme.append(f"| #{num} | {cat_label} | [{title}]({link}) | {author} | {stars} {rating} | {desc} |")
        
        # Add to category grouping
        cat_loops[cat_slug].append(loop)

    # Write root README.md
    with open(os.path.join(REPO_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(readme))

    print("Root README.md compiled successfully.")

    # 2. Compile Category Files
    for cat_slug, list_of_loops in cat_loops.items():
        cat_label = cat_slug.capitalize()
        if len(list_of_loops) > 0:
            cat_label = list_of_loops[0]["category"]["label"]
            
        print(f"Compiling categories/{cat_slug}.md...")
        cat_md = []
        cat_md.append(f"# 🛠️ {cat_label} loops - Loop-Bazaar")
        cat_md.append(f"\nThis directory contains all loops categorized under **{cat_label}**. There are {len(list_of_loops)} loops in this category.")
        cat_md.append("\n[← Back to Master Directory Index](../README.md)")
        cat_md.append("\n---\n")

        # Sort category loops by number index (original chronological order)
        sorted_cat_loops = sorted(list_of_loops, key=lambda l: l.get("number", "0000"))

        for loop in sorted_cat_loops:
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
            
            # HTML Anchor
            cat_md.append(f'## <a name="{slug}">{title}</a>')
            cat_md.append(f"\n- **Number**: #{num}")
            cat_md.append(f"- **Author**: {author}")
            cat_md.append(f"- **Rating**: ⭐ {rating}/5.0")
            cat_md.append(f"- **Published/Modified**: {loop.get('published')} / {loop.get('modified')}")
            
            cat_md.append(f"\n### 📝 Description")
            cat_md.append(desc)
            
            cat_md.append(f"\n### 🎯 Use Case (When to Use)")
            cat_md.append(f"> {use_when}")
            
            cat_md.append(f"\n### ⚡ System Prompt / Instructions")
            cat_md.append("```")
            cat_md.append(prompt)
            cat_md.append("```")
            
            cat_md.append(f"\n### 🏁 Implementation Steps")
            for idx, step in enumerate(loop["steps"]):
                cat_md.append(f"{idx + 1}. {step}")
            
            cat_md.append(f"\n### 🛑 Stopping Condition (Verification)")
            cat_md.append(f"**Verification Check**: {ver_title}")
            cat_md.append(f"- *Detail*: {ver_detail}")
            
            cat_md.append(f"\n### 💡 Why it works")
            cat_md.append(why)
            
            if note:
                cat_md.append(f"\n### ⚠️ Implementation Note")
                cat_md.append(f"* {note}")

            # Reviews
            cat_md.append(f"\n### 💬 Reviews & Comments")
            reviews = loop.get("reviews", [])
            if reviews:
                for r in reviews:
                    stars = "★" * r["rating"] + "☆" * (5 - r["rating"])
                    cat_md.append(f"- **{r['author']}** ({stars} {r['rating']}/5): *{r['comment']}* ({r['date']})")
            else:
                cat_md.append("- *No reviews yet.*")
                
            cat_md.append("\n---\n")

        # Write category file
        with open(os.path.join(CATEGORIES_DIR, f"{cat_slug}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(cat_md))
            
        print(f"categories/{cat_slug}.md compiled successfully.")

if __name__ == "__main__":
    compile_markdown()
