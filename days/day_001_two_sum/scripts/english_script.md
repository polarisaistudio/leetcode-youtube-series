# Day 1: Two Sum (LeetCode #1) - English Script

## Disclaimer
**Educational Content Notice**: This video is for educational purposes only. The solutions and explanations are provided to help you understand algorithmic concepts and prepare for technical interviews. Please ensure you understand the concepts rather than memorizing solutions.

## Opening (30 seconds)

"Welcome back to our LeetCode mastery series! I'm your host, and today we're tackling the classic Two Sum problem - LeetCode problem number 1. This is an Easy level problem, but don't let that fool you - it's one of the most frequently asked questions at companies like Google, Amazon, Facebook, and Microsoft. Let's dive in!"

## Problem Statement (2 minutes)

"Let me read the problem statement:

**Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.**

Let's visualize this with an example:

```
Input Array:  [2,  7,  11, 15]
Indices:       0   1   2   3
Target: 9

Visual Process:
┌─────┬─────┬─────┬─────┐
│  2  │  7  │ 11  │ 15  │  ← Array values
├─────┼─────┼─────┼─────┤
│  0  │  1  │  2  │  3  │  ← Indices
└─────┴─────┴─────┴─────┘

Looking for: ? + ? = 9
Found: 2 + 7 = 9 (indices 0, 1)

Output: [0, 1]
```

Important constraints to note:
- Each input has exactly ONE solution
- You cannot use the same element twice
- The array can have duplicate values
- We need to return the indices, not the values themselves

**Interview Questions I'd Ask:**
```
Q: Can the array be empty?
A: No, minimum 2 elements guaranteed

Q: Are the numbers sorted?
A: No assumption about sorting

Q: Can there be negative numbers?
A: Yes, integers can be negative

Q: What if no solution exists?
A: Problem guarantees exactly one solution
```"

## Solution Approach (4 minutes)

### Approach 1: Brute Force

"The most intuitive approach is to check every pair of numbers:

```
Algorithm Visualization:
Array: [2, 7, 11, 15], Target: 9

Nested Loop Process:
i=0 → j=1: Check 2+7=9  ✓ FOUND!
i=0 → j=2: Check 2+11=13 ✗
i=0 → j=3: Check 2+15=17 ✗
i=1 → j=2: Check 7+11=18 ✗
i=1 → j=3: Check 7+15=22 ✗
i=2 → j=3: Check 11+15=26 ✗

Total Comparisons: n(n-1)/2 = O(n²)
```

**Pseudocode:**
```
For i from 0 to n-1:
    For j from i+1 to n:
        If nums[i] + nums[j] == target:
            return [i, j]
```

**Complexity:**
- Time: O(n²) - nested loops
- Space: O(1) - constant extra space"

### Approach 2: Hash Table (Optimal)

"Here's the key insight: for each number, we know exactly what we're looking for!

```
Hash Table Approach Visualization:
Array: [2, 7, 11, 15], Target: 9

Step-by-step process:
┌─────┬─────────────┬─────────────┬─────────────┐
│Step │ Current Num │ Need (9-x)  │ Hash Table  │
├─────┼─────────────┼─────────────┼─────────────┤
│  1  │     2       │      7      │ {2: 0}      │
│  2  │     7       │      2      │ Found 2!    │
└─────┴─────────────┴─────────────┴─────────────┘

Result: [0, 1] (indices of 2 and 7)
```

**Algorithm Flow:**
1. For each number `x`, calculate `complement = target - x`
2. Check if `complement` exists in hash table
3. If yes → return both indices
4. If no → store `x` and its index in hash table

**Visual Hash Table Operations:**
```
nums = [2, 7, 11, 15], target = 9

i=0: num=2, complement=7
     hash_table = {} 
     7 not found → store: hash_table = {2: 0}

i=1: num=7, complement=2  
     hash_table = {2: 0}
     2 found! → return [hash_table[2], i] = [0, 1]
```"

## Live Coding (7 minutes)

"Let me implement both solutions:

**Solution 1: Brute Force**
```python
def twoSum_bruteforce(nums, target):
    \"\"\"
    Brute force: check all pairs
    Time: O(n²), Space: O(1)
    \"\"\"
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # Never reached per problem constraints
```

**Solution 2: Hash Table (Optimal)**
```python
def twoSum_optimal(nums, target):
    \"\"\"
    Hash table: single pass solution
    Time: O(n), Space: O(n)
    \"\"\"
    seen = {}  # value -> index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # Never reached per problem constraints
```

**Let's trace through examples:**

```
Example 1: nums=[2,7,11,15], target=9
───────────────────────────────────────
i=0, num=2, complement=7
seen = {}, 7 not found
seen = {2: 0}

i=1, num=7, complement=2  
seen = {2: 0}, 2 found!
return [0, 1] ✓

Example 2: nums=[3,2,4], target=6
──────────────────────────────────
i=0, num=3, complement=3
seen = {}, 3 not found
seen = {3: 0}

i=1, num=2, complement=4
seen = {3: 0}, 4 not found  
seen = {3: 0, 2: 1}

i=2, num=4, complement=2
seen = {3: 0, 2: 1}, 2 found!
return [1, 2] ✓
```"

## Complexity Analysis (2 minutes)

"Let's compare our solutions:

```
Complexity Comparison Chart:
┌─────────────┬─────────┬─────────┬─────────────────┐
│   Method    │  Time   │  Space  │   Description   │
├─────────────┼─────────┼─────────┼─────────────────┤
│ Brute Force │  O(n²)  │  O(1)   │ Check all pairs │
│ Hash Table  │  O(n)   │  O(n)   │ Single pass     │
└─────────────┴─────────┴─────────┴─────────────────┘

Time Growth Visualization:
Array Size │ Brute Force │ Hash Table
─────────────────────────────────────
    100     │    10,000   │     100
  1,000     │ 1,000,000   │   1,000  
 10,000     │100,000,000  │  10,000

Space-Time Trade-off:
- Brute Force: No extra space, but O(n²) time
- Hash Table: O(n) extra space, but O(n) time
```

**When to use each:**
- **Brute Force**: When memory is extremely limited
- **Hash Table**: When you need optimal time complexity (99% of cases)"

## Common Pitfalls (1 minute)

"Watch out for these mistakes:

```python
# ❌ WRONG: Using same element twice
def twoSum_wrong(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):  # Should be i+1
            if nums[i] + nums[j] == target:
                return [i, j]

# ❌ WRONG: Returning values instead of indices  
def twoSum_wrong2(nums, target):
    # ... logic ...
    return [nums[i], nums[j]]  # Should return [i, j]

# ❌ WRONG: Not handling duplicates correctly
nums = [3, 3], target = 6
# Should return [0, 1], not skip because values are same

# ✅ CORRECT: Handle edge cases
def twoSum_robust(nums, target):
    if len(nums) < 2:
        return []
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```"

## Related Problems (30 seconds)

"Master Two Sum, then tackle these:

```
Problem Progression:
Two Sum (Easy)           → 3Sum (Medium)         → 4Sum (Medium-Hard)
     ↓                        ↓                        ↓
Two Sum II (Easy)       → 3Sum Closest (Medium) → 4Sum II (Medium)
     ↓                        
Two Sum III (Medium)    
     ↓
Two Sum IV - BST (Easy)

Pattern Recognition:
- Hash Table for unsorted data
- Two Pointers for sorted data  
- Multiple approaches for K-Sum problems
```"

## Interview Tips (1 minute)

"**Interview Strategy:**

1. **Clarify First** (30 seconds)
   ```
   \"Can I assume the array has at least 2 elements?\"
   \"Should I return indices or values?\"
   \"What if there are multiple solutions?\"
   ```

2. **Start Simple** (1 minute)
   ```
   \"Let me start with the brute force approach...\"
   [Implement O(n²) solution]
   ```

3. **Optimize** (2-3 minutes)
   ```
   \"Can we do better? What if we use extra space?\"
   [Implement O(n) solution]
   ```

4. **Test & Debug** (1 minute)
   ```python
   # Test with provided example
   assert twoSum([2,7,11,15], 9) == [0,1]
   # Test edge cases
   assert twoSum([3,3], 6) == [0,1]
   ```

**Expected Follow-ups:**
```
Q: What if array was sorted?
A: Use two pointers - O(n) time, O(1) space

Q: What if we need all pairs?
A: Continue searching after finding first pair

Q: Memory constraints for large arrays?
A: Consider external sorting, distributed processing
```"

## Closing (30 seconds)

"And that's Two Sum! Key takeaways:

✅ Hash tables provide O(1) lookup for complement finding  
✅ Space-time trade-offs are common in optimization  
✅ Always clarify requirements in interviews  
✅ Start simple, then optimize  

Tomorrow we'll explore 'Best Time to Buy and Sell Stock' - another array problem with similar optimization patterns.

Like this video if it helped, subscribe for daily LeetCode content, and drop your questions in the comments! Happy coding! 🚀"

---

**Video Duration**: ~15-18 minutes
**Key Files**: See `images/` folder for visual diagrams
**Next Video**: Day 2 - Best Time to Buy and Sell Stock (#121)