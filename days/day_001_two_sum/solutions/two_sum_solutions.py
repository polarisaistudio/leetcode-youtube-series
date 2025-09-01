"""
Day 1: Two Sum (LeetCode #1)
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

from typing import List
import time

class TwoSumSolutions:
    """
    Multiple approaches to solve the Two Sum problem.
    Each method is implemented with detailed explanations and complexity analysis.
    """
    
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Brute Force
        Check every possible pair of numbers.
        
        Algorithm:
        1. For each element nums[i], check all elements nums[j] where j > i
        2. If nums[i] + nums[j] == target, return [i, j]
        
        Time Complexity: O(n²) - nested loops iterate through all pairs
        Space Complexity: O(1) - only using constant extra space
        
        Visual representation:
        Array: [2, 7, 11, 15], target = 9
        i=0, j=1: 2 + 7 = 9 ✓ Found!
        """
        n = len(nums)
        
        # Check every pair (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # Should never reach here given problem constraints
        return []
    
    def two_sum_hash_table(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 2: Hash Table (One Pass)
        Use a dictionary to store seen numbers and their indices.
        
        Algorithm:
        1. For each number, calculate its complement (target - number)
        2. Check if complement exists in hash table
        3. If yes, return indices; if no, store current number
        
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - hash table can store up to n elements
        
        Visual representation:
        nums = [2, 7, 11, 15], target = 9
        
        i=0: num=2, complement=7, seen={} → seen={2: 0}
        i=1: num=7, complement=2, seen={2: 0} → found! return [0, 1]
        """
        seen = {}  # Dictionary to store {value: index}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our hash table
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        # Should never reach here given problem constraints
        return []
    
    def two_sum_hash_table_two_pass(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 3: Hash Table (Two Pass)
        First pass: build hash table, Second pass: find complement
        
        Algorithm:
        1. First pass: populate hash table with all numbers and indices
        2. Second pass: for each number, check if complement exists
        
        Time Complexity: O(n) - two passes through array
        Space Complexity: O(n) - hash table stores all elements
        
        Note: Less efficient than one-pass version but easier to understand
        """
        num_to_index = {}
        
        # First pass: build the hash table
        for i, num in enumerate(nums):
            num_to_index[num] = i
        
        # Second pass: look for complement
        for i, num in enumerate(nums):
            complement = target - num
            # Make sure we don't use the same element twice
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]
        
        return []
    
    def two_sum_sorted_two_pointers(self, nums: List[int], target: int) -> List[int]:
        """
        Bonus Approach: Two Pointers (if array was sorted)
        This is for interview follow-up: "What if array was sorted?"
        
        Algorithm:
        1. Use two pointers: left at start, right at end
        2. If sum < target, move left pointer right
        3. If sum > target, move right pointer left
        4. If sum == target, found the answer
        
        Time Complexity: O(n log n) for sorting + O(n) for two pointers
        Space Complexity: O(n) for storing original indices
        
        Note: We need to track original indices since problem requires indices
        """
        # Store original indices with values
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()  # Sort by value
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Return original indices in ascending order
                idx1, idx2 = indexed_nums[left][1], indexed_nums[right][1]
                return [min(idx1, idx2), max(idx1, idx2)]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []

def test_all_solutions():
    """
    Comprehensive test suite for all Two Sum solutions.
    Tests various edge cases and validates correctness.
    """
    solution = TwoSumSolutions()
    
    # Test cases with expected results
    test_cases = [
        # Basic cases
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        
        # Edge cases
        ([-1, -2, -3, -4, -5], -8, [2, 4]),  # Negative numbers
        ([0, 4, 3, 0], 0, [0, 3]),           # Zero values
        ([1, 2], 3, [0, 1]),                 # Minimum array size
        
        # Large numbers
        ([1000000000, -1000000000], 0, [0, 1]),
        
        # Duplicates with different targets
        ([2, 5, 5, 11], 10, [1, 2]),
    ]
    
    methods = [
        ("Brute Force", solution.two_sum_brute_force),
        ("Hash Table (One Pass)", solution.two_sum_hash_table),
        ("Hash Table (Two Pass)", solution.two_sum_hash_table_two_pass),
        ("Two Pointers (Sorted)", solution.two_sum_sorted_two_pointers),
    ]
    
    print("🧪 Testing Two Sum Solutions")
    print("=" * 50)
    
    for nums, target, expected in test_cases:
        print(f"\nTest: nums={nums}, target={target}")
        print(f"Expected: {expected}")
        
        for method_name, method in methods:
            try:
                result = method(nums[:], target)  # Use copy to avoid modification
                
                # Validate result (order doesn't matter for indices)
                is_correct = (sorted(result) == sorted(expected) if result and expected 
                            else result == expected)
                
                status = "✅" if is_correct else "❌"
                print(f"  {status} {method_name:25}: {result}")
                
                if not is_correct:
                    print(f"    Expected: {expected}, Got: {result}")
                    
            except Exception as e:
                print(f"  ❌ {method_name:25}: ERROR - {e}")
    
    print("\n" + "=" * 50)

def performance_comparison():
    """
    Compare performance of different approaches with various input sizes.
    """
    import random
    
    solution = TwoSumSolutions()
    
    print("\n⚡ Performance Comparison")
    print("=" * 50)
    print(f"{'Array Size':<12} {'Brute Force':<15} {'Hash Table':<15} {'Ratio':<10}")
    print("-" * 50)
    
    for size in [100, 1000, 5000]:
        # Generate test data
        nums = list(range(size))
        random.shuffle(nums)
        target = nums[0] + nums[1]  # Ensure solution exists
        
        # Time brute force
        start = time.perf_counter()
        solution.two_sum_brute_force(nums, target)
        brute_force_time = time.perf_counter() - start
        
        # Time hash table
        start = time.perf_counter()
        solution.two_sum_hash_table(nums, target)
        hash_table_time = time.perf_counter() - start
        
        ratio = brute_force_time / hash_table_time if hash_table_time > 0 else float('inf')
        
        print(f"{size:<12} {brute_force_time*1000:<15.3f} {hash_table_time*1000:<15.3f} {ratio:<10.1f}x")
    
    print("\nNote: Times are in milliseconds")

def mock_interview_simulation():
    """
    Simulate a technical interview scenario for Two Sum problem.
    """
    print("\n🎯 Mock Interview Simulation")
    print("=" * 50)
    
    print("\n👨‍💼 Interviewer: Let's solve the Two Sum problem.")
    print("Can you explain your approach?")
    
    print("\n👨‍💻 Candidate: I'll start with clarifying questions:")
    print("- Can the array be empty? (No, minimum 2 elements)")
    print("- Should I return indices or values? (Indices)")
    print("- Can there be duplicates? (Yes)")
    print("- Is exactly one solution guaranteed? (Yes)")
    
    print("\n👨‍💻 Candidate: I'll start with brute force...")
    solution = TwoSumSolutions()
    
    print("\nBrute Force Implementation:")
    print("Time: O(n²), Space: O(1)")
    
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.two_sum_brute_force(nums, target)
    print(f"Test: {nums}, target={target} → {result}")
    
    print("\n👨‍💼 Interviewer: Can you optimize it?")
    
    print("\n👨‍💻 Candidate: Yes! I can use a hash table for O(n) solution...")
    print("\nOptimized Implementation:")
    print("Time: O(n), Space: O(n)")
    
    result = solution.two_sum_hash_table(nums, target)
    print(f"Test: {nums}, target={target} → {result}")
    
    print("\n👨‍💼 Interviewer: What if the array was sorted?")
    print("👨‍💻 Candidate: I could use two pointers for O(n) time, O(1) space...")
    
    print("\n👨‍💼 Interviewer: Great! Let's test edge cases.")
    print("👨‍💻 Candidate: Testing with duplicates and negatives...")
    
    edge_cases = [
        ([3, 3], 6),
        ([-1, -2, -3], -5),
        ([0, 4, 3, 0], 0)
    ]
    
    for test_nums, test_target in edge_cases:
        result = solution.two_sum_hash_table(test_nums, test_target)
        print(f"  {test_nums}, target={test_target} → {result}")
    
    print("\n✅ Interview Complete! Key strengths demonstrated:")
    print("- Asked clarifying questions")
    print("- Started with simple solution")  
    print("- Optimized systematically")
    print("- Tested edge cases")
    print("- Discussed trade-offs")

if __name__ == "__main__":
    # Run all tests and demonstrations
    test_all_solutions()
    performance_comparison()
    mock_interview_simulation()
    
    print("\n🎉 Two Sum analysis complete!")
    print("📚 Ready for Day 2: Best Time to Buy and Sell Stock")