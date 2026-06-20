import json
import os
import random

# Source path
src_path = "/root/.gemini/antigravity-cli/brain/63b1e010-619f-4d0c-a04b-0cc19f8234d3/.system_generated/steps/16/content.md"
dest_path = "/root/github-loop-library/loops_data.json"

# Mock feedback comments to seed the loops
mock_comments = [
    ("Alice Chen", 5, "Extremely useful loop! Saved me hours of manual documentation checks."),
    ("Bob Smith", 4, "Works well, but make sure to define the exact metrics before running it."),
    ("Devin Miller", 5, "I run this overnight and it's like having a junior developer working while I sleep."),
    ("Sarah Connor", 4, "Good workflow. Sometimes stalls on large codebase sweeps, but highly recommended."),
    ("James Hook", 3, "Decent loop, but the stopping condition can be a bit ambiguous for legacy code."),
    ("Elena Rostova", 5, "Brilliant stopping condition design. Completely changed our team's workflow."),
    ("Marcus Aurelius", 5, "The discipline this loop introduces to our dev lifecycle is remarkable."),
    ("Ada Lovelace", 5, "An elegant solution to a recurring problem. Clean and deterministic."),
    ("Alan Turing", 4, "Highly logical. It resolved our testing bottlenecks on the first run."),
    ("Grace Hopper", 5, "Tested this in production. It caught three bugs before they hit our users!")
]

def init_db():
    if not os.path.exists(src_path):
        print(f"Source file {src_path} not found.")
        return

    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the start of the JSON
    json_start = content.find("{")
    if json_start == -1:
        print("Could not find JSON object in source file.")
        return

    json_str = content[json_start:]
    data = json.loads(json_str)

    # Process each loop to add ratings and feedback
    for loop in data.get("loops", []):
        # Generate 2 to 4 mock reviews for each loop
        num_reviews = random.randint(2, 4)
        reviews = []
        chosen_comments = random.sample(mock_comments, num_reviews)
        
        total_rating = 0
        for author, base_rating, comment in chosen_comments:
            # Add a slight variation to the rating
            rating = min(5, max(1, base_rating + random.choice([-1, 0, 1])))
            reviews.append({
                "author": author,
                "rating": rating,
                "comment": comment,
                "date": "2026-06-" + str(random.randint(10, 19))
            })
            total_rating += rating
        
        loop["reviews"] = reviews
        loop["averageRating"] = round(total_rating / num_reviews, 1)

    # Save to destination
    with open(dest_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully initialized loops database at {dest_path}")

if __name__ == "__main__":
    init_db()
