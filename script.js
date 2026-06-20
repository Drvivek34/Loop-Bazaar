document.addEventListener("DOMContentLoaded", () => {
  // Constants & State
  const DB_PATH = "loops_data.json";
  let loopsDatabase = [];
  let currentCategory = "all";
  let currentSort = "rating-desc";
  let searchQuery = "";
  
  // Elements
  const themeToggleBtn = document.getElementById("theme-toggle-btn");
  const loopsGrid = document.getElementById("loops-grid");
  const searchInput = document.getElementById("loop-search");
  const clearSearchBtn = document.getElementById("clear-search-btn");
  const searchSuggestions = document.getElementById("search-suggestions");
  const categoryFilters = document.getElementById("category-filters");
  const sortSelect = document.getElementById("loop-sort");
  const resultsCount = document.getElementById("results-count");
  
  // Modals
  const detailModal = document.getElementById("detail-modal");
  const submitModal = document.getElementById("submit-modal");
  const submitLoopBtn = document.getElementById("submit-loop-btn");
  const modalBodyContent = document.getElementById("modal-body-content");
  const submitLoopForm = document.getElementById("submit-loop-form");
  
  // Theme Toggle Initialization
  const savedTheme = localStorage.getItem("loop-library-theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  
  themeToggleBtn.addEventListener("click", () => {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("loop-library-theme", newTheme);
  });

  // Fetch Database
  async function loadDatabase() {
    try {
      const response = await fetch(DB_PATH);
      if (!response.ok) throw new Error("Failed to load database file");
      const data = await response.json();
      loopsDatabase = data.loops || [];
      
      // Load local modifications (user ratings/reviews submitted locally)
      applyLocalModifications();
      
      renderLoops();
      setupSearchSuggestions();
    } catch (error) {
      console.error(error);
      loopsGrid.innerHTML = `
        <div class="error-state">
          <p>⚠️ Error loading loop database. Make sure you are running a local dev server.</p>
        </div>
      `;
    }
  }

  // Local modifications support
  function applyLocalModifications() {
    const localRatings = JSON.parse(localStorage.getItem("loop-local-ratings") || "{}");
    const localSubmissions = JSON.parse(localStorage.getItem("loop-local-submissions") || "[]");
    
    // Add locally submitted loops
    localSubmissions.forEach(sub => {
      if (!loopsDatabase.some(l => l.slug === sub.slug)) {
        loopsDatabase.push(sub);
      }
    });

    // Merge local ratings
    loopsDatabase.forEach(loop => {
      if (localRatings[loop.slug]) {
        localRatings[loop.slug].forEach(review => {
          if (!loop.reviews.some(r => r.comment === review.comment && r.author === review.author)) {
            loop.reviews.push(review);
          }
        });
        
        // Recalculate average rating
        const total = loop.reviews.reduce((sum, r) => sum + r.rating, 0);
        loop.averageRating = roundToOneDecimal(total / loop.reviews.length);
      }
    });
  }

  function roundToOneDecimal(num) {
    return Math.round(num * 10) / 10;
  }

  // Render Loop Cards
  function renderLoops() {
    loopsGrid.innerHTML = "";
    
    // Filter
    let filtered = loopsDatabase.filter(loop => {
      // Category Match
      const matchesCategory = currentCategory === "all" || loop.category.slug === currentCategory;
      
      // Search Match
      const searchLower = searchQuery.toLowerCase();
      const matchesSearch = !searchQuery || 
        loop.title.toLowerCase().includes(searchLower) ||
        loop.description.toLowerCase().includes(searchLower) ||
        loop.prompt.toLowerCase().includes(searchLower) ||
        loop.author.toLowerCase().includes(searchLower) ||
        loop.keywords.some(kw => kw.toLowerCase().includes(searchLower));
        
      return matchesCategory && matchesSearch;
    });

    // Sort
    filtered.sort((a, b) => {
      if (currentSort === "rating-desc") {
        return b.averageRating - a.averageRating || b.reviews.length - a.reviews.length;
      } else if (currentSort === "reviews-desc") {
        return b.reviews.length - a.reviews.length || b.averageRating - a.averageRating;
      } else if (currentSort === "title-asc") {
        return a.title.localeCompare(b.title);
      } else if (currentSort === "title-desc") {
        return b.title.localeCompare(a.title);
      } else if (currentSort === "published-desc") {
        return new Date(b.published) - new Date(a.published);
      }
      return 0;
    });

    resultsCount.textContent = `Showing ${filtered.length} loops`;

    if (filtered.length === 0) {
      loopsGrid.innerHTML = `
        <div class="empty-state">
          <p>🔍 No loops found matching "${searchQuery}" in this category.</p>
        </div>
      `;
      return;
    }

    filtered.forEach(loop => {
      const card = document.createElement("div");
      card.className = "loop-card";
      
      // Star display structure
      const starsHtml = getStarsTemplate(loop.averageRating);

      card.innerHTML = `
        <div class="card-header">
          <span class="card-category cat-${loop.category.slug}">${loop.category.label}</span>
          <span class="rating-badge">${starsHtml} ${loop.averageRating}</span>
        </div>
        <h3>${escapeHtml(loop.title)}</h3>
        <div class="card-author">By ${escapeHtml(loop.author)}</div>
        <p class="card-description">${escapeHtml(loop.description)}</p>
        <div class="card-footer">
          <span class="card-reviews-count">${loop.reviews.length} feedback reviews</span>
          <button class="btn btn-secondary card-view-btn" data-slug="${loop.slug}">View Details</button>
        </div>
      `;
      
      // Attach click to card view details
      card.querySelector(".card-view-btn").addEventListener("click", () => {
        openDetailModal(loop.slug);
      });
      
      loopsGrid.appendChild(card);
    });
  }

  function getStarsTemplate(rating) {
    let stars = "";
    const fullStars = Math.floor(rating);
    const halfStar = rating % 1 >= 0.5;
    
    for (let i = 1; i <= 5; i++) {
      if (i <= fullStars) {
        stars += "★";
      } else if (i === fullStars + 1 && halfStar) {
        stars += "⯪";
      } else {
        stars += "☆";
      }
    }
    return stars;
  }

  // Suggestion Handling
  function setupSearchSuggestions() {
    searchInput.addEventListener("input", () => {
      const value = searchInput.value.trim();
      searchQuery = value;
      
      if (value) {
        clearSearchBtn.style.display = "block";
        const matches = loopsDatabase.filter(loop => 
          loop.title.toLowerCase().includes(value.toLowerCase())
        ).slice(0, 5);
        
        if (matches.length > 0) {
          searchSuggestions.innerHTML = matches.map(loop => `
            <div class="suggestion-item" data-slug="${loop.slug}">
              <span class="suggestion-title">${escapeHtml(loop.title)}</span>
              <span class="suggestion-meta">Category: ${loop.category.label} | Rating: ${loop.averageRating}</span>
            </div>
          `).join("");
          searchSuggestions.classList.remove("hidden");
          
          // Click suggestions
          document.querySelectorAll(".suggestion-item").forEach(item => {
            item.addEventListener("click", () => {
              const slug = item.getAttribute("data-slug");
              searchInput.value = item.querySelector(".suggestion-title").textContent;
              searchQuery = searchInput.value;
              searchSuggestions.classList.add("hidden");
              renderLoops();
              openDetailModal(slug);
            });
          });
        } else {
          searchSuggestions.classList.add("hidden");
        }
      } else {
        clearSearchBtn.style.display = "none";
        searchSuggestions.classList.add("hidden");
      }
      renderLoops();
    });

    // Close suggestions on outside click
    document.addEventListener("click", (e) => {
      if (!searchInput.contains(e.target) && !searchSuggestions.contains(e.target)) {
        searchSuggestions.classList.add("hidden");
      }
    });
  }

  // Clear Search
  clearSearchBtn.addEventListener("click", () => {
    searchInput.value = "";
    searchQuery = "";
    clearSearchBtn.style.display = "none";
    searchSuggestions.classList.add("hidden");
    renderLoops();
  });

  // Filters Selection
  categoryFilters.addEventListener("click", (e) => {
    if (e.target.classList.contains("filter-pill")) {
      document.querySelectorAll(".filter-pill").forEach(pill => pill.classList.remove("active"));
      e.target.classList.add("active");
      currentCategory = e.target.getAttribute("data-category");
      renderLoops();
    }
  });

  // Sorting
  sortSelect.addEventListener("change", (e) => {
    currentSort = e.target.value;
    renderLoops();
  });

  // Modals Open/Close
  submitLoopBtn.addEventListener("click", () => {
    submitModal.classList.remove("hidden");
    submitModal.setAttribute("aria-hidden", "false");
  });

  document.querySelectorAll(".modal-close-btn, .modal-overlay").forEach(btn => {
    btn.addEventListener("click", () => {
      detailModal.classList.add("hidden");
      detailModal.setAttribute("aria-hidden", "true");
      submitModal.classList.add("hidden");
      submitModal.setAttribute("aria-hidden", "true");
    });
  });

  // Open Detail Modal & Dynamic Fill
  function openDetailModal(slug) {
    const loop = loopsDatabase.find(l => l.slug === slug);
    if (!loop) return;

    // Steps list rendering
    const stepsHtml = loop.steps.map((step, idx) => `
      <div class="step-item">
        <span class="step-num">${idx + 1}</span>
        <span class="step-text">${escapeHtml(step)}</span>
      </div>
    `).join("");

    // Keywords rendering
    const keywordsHtml = loop.keywords.map(kw => `
      <span class="keyword-tag">${escapeHtml(kw)}</span>
    `).join("");

    // Reviews list rendering
    const reviewsHtml = loop.reviews.map(review => `
      <div class="review-item">
        <div class="review-meta">
          <span class="review-author">${escapeHtml(review.author)}</span>
          <span class="rating-badge">${"★".repeat(review.rating)}${"☆".repeat(5-review.rating)}</span>
        </div>
        <p class="review-text">${escapeHtml(review.comment)}</p>
      </div>
    `).join("");

    modalBodyContent.innerHTML = `
      <div class="modal-meta-row">
        <span class="card-category cat-${loop.category.slug}">${loop.category.label}</span>
        <span class="rating-badge">${getStarsTemplate(loop.averageRating)} ${loop.averageRating} (${loop.reviews.length} reviews)</span>
        <span style="font-size:12px; opacity:0.6;">Published: ${loop.published}</span>
      </div>
      
      <h2 style="font-size: 28px; margin-bottom: 12px; font-family:'Outfit', sans-serif;">${escapeHtml(loop.title)}</h2>
      <div style="font-size: 13px; color:hsl(var(--text-muted-hsl)); margin-bottom: 24px;">Contributed by <strong>${escapeHtml(loop.author)}</strong></div>

      <div class="modal-section">
        <h4>Description</h4>
        <p style="font-size: 14.5px; color:hsl(var(--text-secondary-hsl));">${escapeHtml(loop.description)}</p>
      </div>

      <div class="modal-section">
        <h4>When to Use</h4>
        <div class="use-case-box">${escapeHtml(loop.useWhen)}</div>
      </div>

      <div class="modal-section">
        <h4>System Prompt / Instructions</h4>
        <div class="prompt-box" id="prompt-content-area">${escapeHtml(loop.prompt)}<span class="copy-badge" id="copy-prompt-btn">Copy Prompt</span></div>
      </div>

      <div class="modal-section">
        <h4>Implementation Steps</h4>
        <div class="steps-list">${stepsHtml}</div>
      </div>

      <div class="modal-section">
        <h4>Verification (Stopping Condition)</h4>
        <p style="font-size:14px; font-weight:600;"><span style="color:hsl(var(--secondary-hsl));">Stop condition:</span> ${escapeHtml(loop.verification.title)} (${escapeHtml(loop.verification.detail)})</p>
      </div>

      <div class="modal-section">
        <h4>Why it works</h4>
        <p style="font-size:13.5px; color:hsl(var(--text-secondary-hsl));">${escapeHtml(loop.why)}</p>
      </div>

      <div class="modal-section">
        <h4>Keywords</h4>
        <div class="keywords-row">${keywordsHtml}</div>
      </div>

      <div class="reviews-section">
        <h3 style="font-size:20px; margin-bottom: 16px; font-family:'Outfit', sans-serif;">Reviews & Feedback</h3>
        <div class="reviews-list">${reviewsHtml || '<p style="font-size:13px; opacity:0.6;">No reviews yet. Be the first to leave feedback!</p>'}</div>
        
        <!-- Feedback Form -->
        <div class="review-form">
          <h4 style="font-size:14px; margin-bottom: 12px; font-weight:700;">Rate this Loop</h4>
          <form id="feedback-form" data-slug="${loop.slug}">
            <div class="form-group" style="margin-bottom:12px;">
              <label>Select Stars</label>
              <div class="rating-input" id="stars-input">
                <span class="star-rating-select" data-rating="1">★</span>
                <span class="star-rating-select" data-rating="2">★</span>
                <span class="star-rating-select" data-rating="3">★</span>
                <span class="star-rating-select" data-rating="4">★</span>
                <span class="star-rating-select" data-rating="5">★</span>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label for="review-author-input">Name *</label>
                <input type="text" id="review-author-input" required placeholder="Your Name">
              </div>
              <div class="form-group">
                <label for="review-comment-input">Comment *</label>
                <input type="text" id="review-comment-input" required placeholder="Describe your experience with this loop">
              </div>
            </div>
            <div style="margin-top: 16px; display:flex; gap:12px;">
              <button type="submit" class="btn btn-primary">Submit Rating & Leave Comment</button>
              <button type="button" id="github-feedback-btn" class="btn btn-secondary">Submit on GitHub</button>
            </div>
          </form>
        </div>
      </div>
    `;

    detailModal.classList.remove("hidden");
    detailModal.setAttribute("aria-hidden", "false");

    // Copy Prompt functionality
    const copyBtn = document.getElementById("copy-prompt-btn");
    copyBtn.addEventListener("click", () => {
      navigator.clipboard.writeText(loop.prompt).then(() => {
        copyBtn.textContent = "Copied!";
        copyBtn.style.backgroundColor = "hsl(var(--secondary-hsl))";
        copyBtn.style.color = "black";
        setTimeout(() => {
          copyBtn.textContent = "Copy Prompt";
          copyBtn.style.backgroundColor = "";
          copyBtn.style.color = "";
        }, 2000);
      });
    });

    // Rating star inputs logic
    let selectedRating = 0;
    const starSpans = document.querySelectorAll("#stars-input .star-rating-select");
    
    starSpans.forEach(star => {
      star.addEventListener("click", () => {
        selectedRating = parseInt(star.getAttribute("data-rating"));
        updateStarsDisplay(selectedRating);
      });
      star.addEventListener("mouseover", () => {
        updateStarsDisplay(parseInt(star.getAttribute("data-rating")));
      });
    });

    document.getElementById("stars-input").addEventListener("mouseleave", () => {
      updateStarsDisplay(selectedRating);
    });

    function updateStarsDisplay(rating) {
      starSpans.forEach(s => {
        const val = parseInt(s.getAttribute("data-rating"));
        if (val <= rating) {
          s.classList.add("active");
        } else {
          s.classList.remove("active");
        }
      });
    }

    // Submit Local Review
    const feedbackForm = document.getElementById("feedback-form");
    feedbackForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (selectedRating === 0) {
        alert("Please select a star rating!");
        return;
      }

      const author = document.getElementById("review-author-input").value.trim();
      const comment = document.getElementById("review-comment-input").value.trim();
      
      const newReview = {
        author,
        rating: selectedRating,
        comment,
        date: new Date().toISOString().split("T")[0]
      };

      // Save to localStorage
      const localRatings = JSON.parse(localStorage.getItem("loop-local-ratings") || "{}");
      if (!localRatings[slug]) localRatings[slug] = [];
      localRatings[slug].push(newReview);
      localStorage.setItem("loop-local-ratings", JSON.stringify(localRatings));

      // Update UI state & refresh
      applyLocalModifications();
      renderLoops();
      
      // Close modal
      detailModal.classList.add("hidden");
      detailModal.setAttribute("aria-hidden", "true");
      alert("Feedback saved locally! Submit on GitHub to make it permanent for everyone.");
    });

    // Submit via GitHub Issue
    document.getElementById("github-feedback-btn").addEventListener("click", () => {
      const author = document.getElementById("review-author-input").value.trim() || "Anonymous";
      const comment = document.getElementById("review-comment-input").value.trim() || "No comment";
      const stars = selectedRating || 5;

      const issueTitle = encodeURIComponent(`Feedback: ${loop.slug}`);
      const issueBody = encodeURIComponent(
        `## Loop Feedback\n` +
        `- **Loop**: ${loop.title} (${loop.slug})\n` +
        `- **Rating**: ${stars}/5 Stars\n` +
        `- **Author**: ${author}\n` +
        `- **Feedback**: ${comment}\n\n` +
        `*Submitted via Loop Library UI*`
      );

      const githubUrl = `https://github.com/Drvivek34/github-loop-library/issues/new?title=${issueTitle}&body=${issueBody}&labels=feedback`;
      window.open(githubUrl, "_blank");
    });
  }

  // Submit New Loop Form Submission to GitHub
  submitLoopForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = document.getElementById("form-title").value.trim();
    const category = document.getElementById("form-category").value;
    const author = document.getElementById("form-author").value.trim();
    const description = document.getElementById("form-description").value.trim();
    const prompt = document.getElementById("form-prompt").value.trim();
    const stepsText = document.getElementById("form-steps").value.trim();
    const verification = document.getElementById("form-verification").value.trim();

    const steps = stepsText.split("\n").map(s => s.trim()).filter(s => s.length > 0);

    const issueTitle = encodeURIComponent(`Submission: ${title}`);
    const issueBody = encodeURIComponent(
      `## Loop Submission Details\n` +
      `- **Title**: ${title}\n` +
      `- **Category**: ${category}\n` +
      `- **Author**: ${author}\n` +
      `- **Description**: ${description}\n` +
      `- **Verification**: ${verification}\n\n` +
      `### Prompt / Instructions\n` +
      `\`\`\`\n${prompt}\n\`\`\`\n\n` +
      `### Implementation Steps\n` +
      steps.map(s => `- ${s}`).join("\n") + `\n\n` +
      `*Submitted via Loop Library Submit Form*`
    );

    const githubUrl = `https://github.com/Drvivek34/github-loop-library/issues/new?title=${issueTitle}&body=${issueBody}&labels=submission`;
    
    // Save locally as well so it shows immediately
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
    const newLocalLoop = {
      number: "LOCAL-" + Date.now().toString().slice(-4),
      slug,
      title,
      url: "#",
      category: {
        slug: category,
        label: category.charAt(0).toUpperCase() + category.slice(1)
      },
      author,
      published: new Date().toISOString().split("T")[0],
      modified: new Date().toISOString().split("T")[0],
      description,
      useWhen: description,
      prompt,
      verification: {
        title: verification,
        detail: "Standard run checks"
      },
      steps,
      why: "Community contributed loop.",
      implementationNote: "Standard implementation.",
      keywords: [category, "community-submission"],
      reviews: [],
      averageRating: 5.0
    };

    const localSubmissions = JSON.parse(localStorage.getItem("loop-local-submissions") || "[]");
    localSubmissions.push(newLocalLoop);
    localStorage.setItem("loop-local-submissions", JSON.stringify(localSubmissions));

    // Reload Database & grid
    applyLocalModifications();
    renderLoops();
    
    // Close Modal
    submitModal.classList.add("hidden");
    submitModal.setAttribute("aria-hidden", "true");
    
    // Open GitHub tab
    window.open(githubUrl, "_blank");
    alert("Local submission created! Now please submit the pre-filled issue on GitHub to update the global library.");
  });

  // Helper Escapes
  function escapeHtml(str) {
    if (!str) return "";
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  // Load App
  loadDatabase();
});
