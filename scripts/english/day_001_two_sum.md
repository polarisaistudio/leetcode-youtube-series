# Day 1: Two Sum (LeetCode #1)

## Opening (30 seconds)

"Welcome back to our LeetCode mastery series! I'm your host, and today we're tackling the classic Two Sum problem - LeetCode problem number 1. This is an Easy level problem, but don't let that fool you - it's one of the most frequently asked questions at companies like Google, Amazon, Facebook, and Microsoft. Let's dive in!"

## Problem Statement (2 minutes)

"Let me read the problem statement:

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Let's look at an example to understand this better.

[Reference: illustration_1_two_sum_example.png]

If we have nums = [2, 7, 11, 15] and target = 9, we need to find two numbers that add up to 9. We can see that 2 + 7 = 9, and these are at indices 0 and 1, so we return [0, 1].

Important constraints to note:
- Each input has exactly ONE solution
- You cannot use the same element twice
- The array can have duplicate values
- We need to return the indices, not the values themselves

In an interview, I would ask:
- Can the array be empty? (No, minimum 2 elements)
- Are the numbers sorted? (No, they're not)
- Can there be negative numbers? (Yes)
- What should we return if no solution exists? (Problem guarantees a solution)"

## Solution Approach (4 minutes)

### Approach 1: Brute Force

"The most intuitive approach is to check every pair of numbers.

[Reference: illustration_2_brute_force.png]

For each element, we check it against every other element to see if they sum to our target. This works, but it's not efficient.

```
For i from 0 to n-1:
    For j from i+1 to n:
        If nums[i] + nums[j] == target:
            return [i, j]
```

Time Complexity: O(n²) - we have nested loops
Space Complexity: O(1) - we only use a constant amount of extra space"

### Approach 2: Hash Table (Optimal)

"Here's the key insight: for each number, we know exactly what number we're looking for - it's `target - current_number`. Instead of searching for it, we can store numbers we've seen in a hash table!

[Reference: illustration_3_hash_table.png]

As we iterate through the array:
1. Calculate the complement: `complement = target - current_number`
2. Check if the complement exists in our hash table
3. If yes, we found our pair! Return the indices
4. If no, add the current number and its index to the hash table

This single pass solution is much more efficient!"

## Live Coding (7 minutes)

"Let me code both solutions, starting with the brute force approach to show the progression:

```python
def twoSum_bruteforce(nums, target):
    n = len(nums)
    # Check every pair of numbers
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # This line should never be reached given problem constraints
```

Now, let's implement the optimized hash table solution:

```python
def twoSum(nums, target):
    # Dictionary to store value -> index mapping
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate what number we need
        complement = target - num
        
        # Check if we've seen this complement before
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    return []  # This line should never be reached
```

Let's trace through our example:
- nums = [2, 7, 11, 15], target = 9
- i=0, num=2, complement=7, seen={}, 7 not in seen, add 2->0
- i=1, num=7, complement=2, seen={2:0}, 2 IS in seen! Return [0, 1]

Perfect! Let's test with another example:
- nums = [3, 2, 4], target = 6
- i=0, num=3, complement=3, seen={}, add 3->0
- i=1, num=2, complement=4, seen={3:0}, add 2->1
- i=2, num=4, complement=2, seen={3:0, 2:1}, 2 IS in seen! Return [1, 2]"

## Complexity Analysis (2 minutes)

"Let's break down the complexity:

[Reference: illustration_4_complexity_comparison.png]

**Brute Force:**
- Time: O(n²) - For each element, we check n-1 other elements
- Space: O(1) - No extra space needed

**Hash Table:**
- Time: O(n) - Single pass through the array
- Space: O(n) - In worst case, we store all n elements in the hash table

The trade-off here is classic: we sacrifice space for time. In most cases, the O(n) time complexity is worth the extra O(n) space."

## Common Pitfalls (1 minute)

"Watch out for these common mistakes:

1. **Using the same element twice**: Make sure your second loop starts at i+1, not i
2. **Returning values instead of indices**: The problem asks for indices!
3. **Not handling duplicates correctly**: [3, 3] with target 6 should return [0, 1]
4. **Edge case with negative numbers**: [-1, -2, -3, -4, -5] with target -8
5. **Forgetting to store the index in the hash table**: We need both value and index"

## Related Problems (30 seconds)

"Once you master Two Sum, try these related problems:
- 3Sum (LeetCode #15) - Extension to three numbers
- 4Sum (LeetCode #18) - Extension to four numbers
- Two Sum II (LeetCode #167) - When array is sorted
- Two Sum III (LeetCode #170) - Data structure design
- Two Sum IV (LeetCode #653) - In a BST"

## Interview Tips (1 minute)

"In an interview setting:

1. **Start with clarifying questions** - Shows attention to detail
2. **Discuss the brute force first** - Shows you can think of a solution quickly
3. **Optimize step by step** - Demonstrates problem-solving process
4. **Think out loud** - Interviewers want to understand your thought process
5. **Test your code** - Walk through an example before saying you're done

Follow-up questions to expect:
- What if the array is sorted? (Can use two pointers - O(n) time, O(1) space)
- What if we need all pairs that sum to target? (Continue searching after finding first)
- How would you handle very large arrays? (Discuss memory constraints)
- Can you solve it with O(1) space? (Only if sorted - use two pointers)"

## Closing (30 seconds)

"And that's Two Sum! We've covered two approaches, analyzed complexity, and discussed interview strategies. The key takeaway: hash tables are powerful for finding pairs and complements. 

Tomorrow, we'll tackle 'Best Time to Buy and Sell Stock' - another array problem that builds on today's concepts. 

If you found this helpful, please like and subscribe! Drop a comment with any questions, and remember - consistent practice is the key to mastering these problems. See you tomorrow!"