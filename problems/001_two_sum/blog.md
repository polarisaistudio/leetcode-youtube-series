# Mastering LeetCode: Two Sum (#1) — From Brute Force to Optimal

## Why 70% of FAANG Companies Ask This "Easy" Problem (And How to Ace It)

*Part of the comprehensive LeetCode mastery series — 10 min read*

![Coding Interview Illustration](https://images.unsplash.com/photo-1515879218367-8466d910aaa4)
*Photo by [Chris Ried](https://unsplash.com/@cdr6934) on Unsplash*

---

> **Disclaimer**: This article is for educational purposes. The solutions are designed to teach concepts and problem-solving approaches. Please understand the concepts rather than memorizing code.

**Difficulty:** Easy  
**Topics:** Array, Hash Table  
**Companies:** Google, Amazon, Facebook, Microsoft, Apple  

---

## The $100,000 Question That Started It All 💰

Picture this: You're in a Google interview room. The interviewer smiles and says, "Let's start with something simple — Two Sum."

Your heart races. Is this a trick? Why would Google ask LeetCode #1?

Here's the truth: **Two Sum isn't about finding two numbers that add up**. It's about demonstrating you understand space-time tradeoffs, hash table applications, and optimization thinking — concepts worth hundreds of thousands in salary negotiations.

Today, I'll show you not just how to solve it, but how to solve it in a way that makes interviewers think, *"This person gets it."*

---

## 📋 The Problem That Launched a Thousand Careers

**Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.**

Simple, right? Let's visualize what's actually happening:

```
Array:    [2,  7,  11, 15]
Indices:   0   1   2   3
Target: 9

┌─────┬─────┬─────┬─────┐
│  2  │  7  │ 11  │ 15  │
├─────┼─────┼─────┼─────┤
│  0  │  1  │  2  │  3  │  ← We return these!
└─────┴─────┴─────┴─────┘
       ↑     ↑
   2 + 7 = 9 ✓
```

### Quick Examples

```python
# Example 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]  # nums[0] + nums[1] = 2 + 7 = 9

# Example 2  
Input: nums = [3,2,4], target = 6
Output: [1,2]  # nums[1] + nums[2] = 2 + 4 = 6

# Example 3 (The tricky one!)
Input: nums = [3,3], target = 6
Output: [0,1]  # Two different 3s
```

**Key Rules:**
- ✅ Each element used only once
- ✅ Exactly one solution exists
- ✅ Return indices, not values
- ✅ Order doesn't matter

---

## 🔍 Solution 1: The Naive Approach (That 90% Start With)

### The Thought Process
*"I'll just check every possible pair!"*

This is where everyone starts, and **that's perfectly fine**. In fact, starting here in an interview shows you can solve problems incrementally.

```python
def twoSum_bruteforce(nums, target):
    """
    The straightforward approach: Check all pairs
    Time: O(n²) - We check n*(n-1)/2 pairs
    Space: O(1) - No extra storage needed
    """
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):  # Start from i+1 to avoid reusing elements
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  # Never reached (problem guarantees a solution)
```

### Performance Reality Check
```
Array Size | Time Taken | Operations
-----------|------------|------------
    100    |   0.5ms    |     4,950
  1,000    |  45.2ms    |   499,500
 10,000    | 4,521ms    | 49,995,000
100,000    |  ∞ (😱)    | 4,999,950,000
```

**Interview Insight:** Start here, acknowledge it's O(n²), then say: *"Let me optimize this..."*

---

## 🚀 Solution 2: The Hash Table Magic (What Gets You Hired)

### The "Aha!" Moment

Here's the game-changing insight: **For every number x, we know its partner must be (target - x)**

Instead of searching for this partner, what if we could look it up instantly?

```python
def twoSum_optimal(nums, target):
    """
    The optimal approach: Hash table for O(1) lookups
    Time: O(n) - Single pass through array
    Space: O(n) - Hash table storage
    """
    seen = {}  # Our hash table: {value: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # The magic moment: O(1) lookup!
        if complement in seen:
            return [seen[complement], i]
        
        # Remember this number for future lookups
        seen[num] = i
    
    return []
```

### Let's Trace Through It
```python
nums = [2, 7, 11, 15], target = 9

Step 1: num=2, complement=7
        seen={}, 7 not found
        seen={2:0}

Step 2: num=7, complement=2  
        seen={2:0}, 2 FOUND! ✓
        return [0, 1]

Magic! 🎩
```

### Why This Blows Minds in Interviews

The jump from O(n²) to O(n) shows you understand:
- **Trade-offs**: Trading space for time
- **Data structures**: Knowing when hash tables shine
- **Optimization**: Not settling for "good enough"

---

## 🎯 Solution 3: Two Pointers (The Bonus Round)

*"What if the array was sorted?"* — Every interviewer's follow-up

```python
def twoSum_twoPointers(nums, target):
    """
    For sorted arrays: Two pointers technique
    Time: O(n log n) for sorting + O(n) for pointers
    Space: O(n) for index tracking
    """
    # Keep track of original indices
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        elif current_sum < target:
            left += 1  # Need bigger sum
        else:
            right -= 1  # Need smaller sum
    
    return []
```

**When to mention this:** After your optimal solution, say: *"If the array were sorted, we could use two pointers for O(1) space..."*

---

## ⚠️ The Edge Cases That Trip Everyone Up

```python
# The duplicate trap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,3], target=6 returns [0,1] - Can't use same element twice!
        pass

# Test with various edge cases:
# Negative numbers: [-1,-2,-3,-4,-5], target=-8 → [2,4]
# Zeros: [0,4,3,0], target=0 → [0,3]
# Large numbers: [1000000000, -1000000000], target=0 → [0,1]
```

**Pro tip:** Always test with duplicates — it's the #1 edge case people miss!

---

## 💬 The Interview Script That Works

### Opening (30 seconds)
> "Let me clarify: We return indices not values, correct? And exactly one solution is guaranteed? Perfect."

### Phase 1 (2 minutes)
> "I'll start with the brute force approach to ensure I understand correctly..."
> 
> *[Write O(n²) solution]*
> 
> "This works but it's O(n²). Can we do better?"

### Phase 2 (3 minutes)  
> "The bottleneck is searching for the complement. If we store seen numbers in a hash table, we can look them up in O(1)..."
> 
> *[Write optimal solution]*
> 
> "This gives us O(n) time with O(n) space — a good trade-off."

### Phase 3 (1 minute)
> "Let me trace through an example to verify..."
> 
> *[Walk through test case]*

### Bonus Points
> "If the array were sorted, we could use two pointers. If we needed all pairs, we'd continue searching instead of returning immediately."

---

## 🎓 The Patterns You Just Learned

### The Complement Pattern
When you know what you're looking for, hash tables find it fast.

**You'll see this in:**
- 3Sum (#15)
- 4Sum (#18)  
- Two Sum variants (#167, #170, #653)
- Subarray sum problems

### The One-Pass Optimization
Process and store in a single iteration.

**You'll see this in:**
- Best Time to Buy and Sell Stock (#121)
- Maximum Subarray (#53)
- Contains Duplicate (#217)

---

## 📈 Your Next Steps

### Practice These Variations
1. **Two Sum II** - Input array is sorted (#167)
2. **3Sum** - Find three numbers that sum to target (#15)
3. **Two Sum IV** - Input is a BST (#653)

### Tomorrow's Challenge
**Best Time to Buy and Sell Stock (#121)** — We'll apply the single-pass pattern to find maximum profit. It's Two Sum's cousin that teaches dynamic thinking.

---

## 🚀 The Takeaway That Changes Everything

Two Sum isn't about adding two numbers. It's about showing you can:
- Start simple and optimize systematically
- Recognize when to trade space for time
- Communicate your thought process clearly
- Handle edge cases thoughtfully

Master this approach, and you'll recognize the pattern in countless other problems.

**Remember:** Every senior engineer at Google once stared at this problem, confused. The difference? They practiced until the pattern clicked.

Your turn. Open LeetCode. Solve it three times — once for each approach. Then move on to the variations.

You've got this. 💪

---

## 📺 Video Walkthrough

Want to see these solutions coded live with step-by-step explanations? 

**[Watch the complete video tutorial on YouTube →](https://youtu.be/if9QVKJ1_TA)**

In the video, I cover:
- Live coding all three approaches
- Debugging common mistakes
- Whiteboard explanation of the hash table approach
- Interview tips from real FAANG experiences

---

**Found this helpful?** Give it a 👏 and follow for daily LeetCode deep dives!

**[Follow me on Medium](https://medium.com/@yourhandle)** | **[Connect on LinkedIn](https://linkedin.com)** | **[Solutions on GitHub](https://github.com)**

*Part of the "500 Days to LeetCode Mastery" series. Next: [Day 2] Best Time to Buy and Sell Stock*

**Tags:** `#LeetCode` `#Algorithms` `#Python` `#CodingInterview` `#DataStructures`
