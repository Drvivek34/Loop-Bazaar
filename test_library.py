import unittest
import json
import os

class TestLoopsDatabase(unittest.TestCase):
    def setUp(self):
        self.db_path = "/root/github-loop-library/loops_data.json"
        self.assertTrue(os.path.exists(self.db_path), "Database file loops_data.json does not exist")
        
        with open(self.db_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_schema_version(self):
        self.assertIn("schemaVersion", self.data)
        self.assertEqual(self.data["schemaVersion"], 1)

    def test_loops_exist(self):
        self.assertIn("loops", self.data)
        self.assertTrue(isinstance(self.data["loops"], list))
        self.assertGreater(len(self.data["loops"]), 0, "No loops found in the database")

    def test_loop_properties(self):
        required_keys = [
            "number", "slug", "title", "category", "author", 
            "published", "modified", "description", "prompt", 
            "verification", "steps", "why", "keywords", 
            "reviews", "averageRating"
        ]
        
        valid_categories = ["engineering", "evaluation", "operations", "content", "design"]

        for idx, loop in enumerate(self.data["loops"]):
            # Check required keys
            for key in required_keys:
                self.assertIn(key, loop, f"Loop at index {idx} ({loop.get('title', 'Unknown')}) is missing required key '{key}'")
            
            # Check slug format
            slug = loop["slug"]
            self.assertTrue(slug.islower(), f"Slug '{slug}' must be lowercase")
            self.assertNotIn(" ", slug, f"Slug '{slug}' must not contain spaces")

            # Check category format
            category = loop["category"]
            self.assertIn("slug", category)
            self.assertIn("label", category)
            self.assertIn(category["slug"], valid_categories, f"Invalid category slug '{category['slug']}' in loop '{loop['title']}'")

            # Check prompt and steps
            self.assertTrue(len(loop["prompt"]) > 0, f"Prompt must not be empty in loop '{loop['title']}'")
            self.assertTrue(isinstance(loop["steps"], list), f"Steps must be a list in loop '{loop['title']}'")
            self.assertGreater(len(loop["steps"]), 0, f"Steps list must contain at least one step in loop '{loop['title']}'")

            # Check ratings and reviews
            self.assertTrue(isinstance(loop["reviews"], list), f"Reviews must be a list in loop '{loop['title']}'")
            self.assertTrue(isinstance(loop["averageRating"], (int, float)), f"averageRating must be a number in loop '{loop['title']}'")
            self.assertTrue(1.0 <= loop["averageRating"] <= 5.0, f"averageRating must be between 1.0 and 5.0 in loop '{loop['title']}'")

            for r_idx, review in enumerate(loop["reviews"]):
                self.assertIn("author", review, f"Review {r_idx} in loop '{loop['title']}' is missing 'author'")
                self.assertIn("rating", review, f"Review {r_idx} in loop '{loop['title']}' is missing 'rating'")
                self.assertIn("comment", review, f"Review {r_idx} in loop '{loop['title']}' is missing 'comment'")
                self.assertTrue(1 <= review["rating"] <= 5, f"Rating in review {r_idx} in loop '{loop['title']}' must be between 1 and 5")

if __name__ == "__main__":
    unittest.main()
