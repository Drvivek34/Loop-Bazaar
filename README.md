# ∞ AI Agent Loop Library

A premium, interactive, and community-driven directory of reusable AI coding and agent workflows. It lists repeatable prompts, execution check-steps, and concrete stopping (verification) conditions, categorized and ranked by community feedback.

The library updates automatically **every day at 6:00 AM** by scraping the latest workflows from the web, verifying pull requests, and processing feedback issues/submissions.

## 🚀 Live Demo & Tech Stack
The dashboard is built entirely with clean, premium vanilla technologies for maximum performance, responsiveness, and zero dependency issues:
- **Core**: Semantic HTML5 & Modern ES6 JavaScript.
- **Styling**: Responsive Vanilla CSS featuring a dark-mode by default glassmorphism theme, glowing background elements, fluid animations, and custom scrollbars.
- **Data Engine**: A structured JSON database (`loops_data.json`) that stores all catalog metadata, ratings, and comments.

---

## 💎 Features & Rankings

1. **Rich Aesthetics**: A visually stunning dashboard, styled with deep space radial gradients, responsive CSS grids, and smooth interaction states.
2. **Search with Autocomplete**: Search by title, summary, keyword, or author with an instant dropdown suggestion list.
3. **Advanced Categorization**: Filter loops across five core agent capabilities:
   - **Engineering**: Code creation, refactoring, and documentation audits.
   - **Evaluation**: Quality streaks, prompt tuning, and regression benchmarks.
   - **Operations**: Releases, data cleanup, and repository hygiene.
   - **Content**: SEO visibility sweeps and media generation.
   - **Design**: Web design reconstruction and vision benchmark rigs.
4. **Sortable Rankings**: Sort the library dynamically by:
   - **Highest Rated**: Ranked by average star ratings.
   - **Most Reviewed**: Ranked by volume of community reviews and discussions.
   - **Newest Added**: See what loops were added recently.
   - **Title (A-Z / Z-A)**: Standard alphabetical sort.
5. **Interactive Rating & Comments Panel**: Star rating selections (1-5 stars) and feedback reviews on each loop modal.

---

## 🤖 6:00 AM Automation & GitHub Integrations

A scheduled background job runs daily at **6:00 AM Asia/Kolkata (IST)** executing `daily_run.sh` which runs `update_library.py`. This script handles autonomous repository maintenance:

### 1. External Web Scraping
The script scrapes the latest loops from external sources (starting with the Forward Future loop catalog) and adds any newly discovered loops to the library database.

### 2. Autonomous Pull Request Verification
- The script checks out open Pull Requests on the repository using the GitHub CLI (`gh pr checkout`).
- It runs the unit test suite (`python3 -m unittest test_library.py`) to verify that modifications to the database schema or frontend files are valid and don't break the system.
- **If tests pass**: The script automatically merges the PR and deletes the source branch.
- **If tests fail**: It leaves a detailed feedback comment on the PR indicating the failure, leaving it open for revision.

### 3. Automatic Feedback & submissions Processing (Issues)
The script triages open issues looking for labeled submissions and feedback:
- **Loop Submissions**: Issues labeled `submission` or prefixed with `Submission:` are parsed. The script extracts the title, category, description, prompt, steps, and verification conditions, assigns it a sequential loop ID, registers it into the database, commits the file, and closes the issue.
- **Review Ratings/Feedback**: Issues labeled `feedback` or prefixed with `Feedback:` are parsed for ratings (1-5 stars) and comment text. The database updates the loop reviews list, recalculates the average rating, and closes the issue automatically.
- **General Issues (Autonomous Fixing)**: For general bug reports or feature requests, if a `GEMINI_API_KEY` is present, the script uses the Gemini API to analyze the codebase and issue description, writes a code fix, runs the unit test suite to verify correctness, and commits the fix before closing the issue.

---

## 🛠️ Local Development & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Drvivek34/github-loop-library.git
   cd github-loop-library
   ```

2. **Run a Local Server**:
   Because the frontend fetches `loops_data.json` dynamically, you must host it on a local server to avoid CORS blocks:
   ```bash
   # Python 3
   python3 -m http.server 8000
   
   # Node.js
   npx http-server -p 8000
   ```
   Now visit `http://localhost:8000` in your browser.

3. **Running Database Unit Tests**:
   ```bash
   python3 -m unittest test_library.py
   ```

4. **Testing the Daily Update Script manually**:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"  # Optional, for issue auto-fixing
   python3 update_library.py
   ```

---

## 🤝 How to Contribute

- **Submit a Loop**: Click the "Submit a Loop" button in the navigation header. Fill out the form, which will generate a link to open a pre-filled GitHub Issue.
- **Rate a Loop**: Click "View Details" on any loop card, scroll to the "Reviews & Feedback" section, fill in your review, and click "Submit on GitHub" to open the issue template.
