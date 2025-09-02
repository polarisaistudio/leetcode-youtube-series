# LeetCode Blog Series 📝

A comprehensive collection of LeetCode problem solutions with detailed blog posts ready for Medium publication.

## 🎯 Purpose

Generate high-quality technical blog posts for LeetCode problems with:
- Multiple solution approaches
- Detailed complexity analysis
- Visual diagrams using Mermaid
- Interview tips and patterns
- Production-ready Python code

## 📁 Simple Structure

```
leetcode-blog-series/
├── problems/           # All problems organized by number
│   └── 001_two_sum/   # Example problem folder
│       ├── blog.md    # Ready-to-publish blog post
│       ├── solution.py # Python solutions with tests
│       └── diagrams.md # Mermaid visualizations
├── templates/         # Blog post template
└── schedules/         # Problem roadmap
```

## 🚀 Quick Start

### Example: Two Sum (Problem #1)
```bash
# View the blog post
cat problems/001_two_sum/blog.md

# Run the solution
python3 problems/001_two_sum/solution.py

# View diagrams (renders on GitHub)
open problems/001_two_sum/diagrams.md
```

## 📝 Blog Publishing Guide

### For Medium
1. Copy content from `problems/XXX/blog.md`
2. For diagrams: Use [mermaid.live](https://mermaid.live) to export as images
3. Add tags: `#LeetCode #Algorithms #Python #Programming #TechnicalInterview`
4. Publish!

### For Dev.to
- Supports Mermaid natively - paste diagram code directly from `diagrams.md`

### For Personal Blog
- Use the markdown directly or convert to HTML
- Include mermaid.js for diagram rendering

## 📊 Problem Schedule

### Phase 1: Fundamentals (Problems 1-30)
Focus on arrays, strings, and basic data structures

### Phase 2: Intermediate (Problems 31-150)
Trees, graphs, dynamic programming

### Phase 3: Advanced (Problems 151-500)
Complex algorithms and system design

See `schedules/` for the complete 500-problem roadmap.

## ✅ What Each Problem Includes

Every problem folder contains:

1. **blog.md** - Complete blog post (2000-3000 words)
   - Problem explanation
   - Multiple solutions (brute force → optimal)
   - Complexity analysis
   - Code walkthrough
   - Interview tips
   - Related problems

2. **solution.py** - Working Python code
   - Multiple approaches
   - Test cases
   - Performance comparison
   - Mock interview simulation

3. **diagrams.md** - Visual explanations
   - Algorithm flowcharts
   - Complexity comparisons
   - Step-by-step traces
   - Pattern recognition

## 🎨 Creating New Problems

Use the template to create new problem posts:
```bash
# Copy template
cp templates/blog_template.md problems/002_add_two_numbers/blog.md

# Edit with your solution
# Add Python code
# Create diagrams
```

## 📈 Progress Tracking

- [x] Problem 1: Two Sum
- [ ] Problem 2: Add Two Numbers
- [ ] Problem 3: Longest Substring Without Repeating Characters
- [ ] ... 497 more problems

## 🤝 Contributing

1. Pick a problem from the schedule
2. Create a folder: `problems/XXX_problem_name/`
3. Write the blog post using the template
4. Add working Python solutions
5. Create Mermaid diagrams
6. Submit a pull request

## 📜 License

MIT License - Use freely for learning and blog creation.

---

**Focus**: Simple, clean blog content generation for LeetCode problems.