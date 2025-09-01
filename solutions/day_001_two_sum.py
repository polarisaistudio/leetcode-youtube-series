"""
Day 1: Two Sum (LeetCode #1)
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.
"""

from typing import List

class Solution:
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Brute Force
        Check every pair of numbers
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def twoSum_optimal(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 2: Hash Table (One Pass)
        Use a dictionary to store seen numbers and their indices
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}  # value -> index mapping
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []
    
    def twoSum_two_pass(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 3: Hash Table (Two Pass)
        First pass: build the hash table
        Second pass: look for complement
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_map = {}
        
        # First pass: populate the hash table
        for i, num in enumerate(nums):
            num_map[num] = i
        
        # Second pass: look for complement
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        
        return []
    
    def twoSum_sorted(self, nums: List[int], target: int) -> List[int]:
        """
        Bonus: If array was sorted (for interview follow-up)
        Use two pointers approach
        
        Time Complexity: O(n log n) for sorting + O(n) for search
        Space Complexity: O(n) for storing original indices
        """
        # Store original indices before sorting
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()  # Sort by value
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []


def test_solutions():
    """Test all solutions with various test cases"""
    solution = Solution()
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]
    
    for nums, target, expected in test_cases:
        print(f"Testing nums={nums}, target={target}")
        
        # Test brute force
        result1 = solution.twoSum_bruteforce(nums[:], target)
        assert sorted(result1) == sorted(expected), f"Brute force failed: {result1}"
        print(f"  Brute force: {result1} ✓")
        
        # Test optimal
        result2 = solution.twoSum_optimal(nums[:], target)
        assert sorted(result2) == sorted(expected), f"Optimal failed: {result2}"
        print(f"  Optimal: {result2} ✓")
        
        # Test two-pass
        result3 = solution.twoSum_two_pass(nums[:], target)
        assert sorted(result3) == sorted(expected), f"Two-pass failed: {result3}"
        print(f"  Two-pass: {result3} ✓")
        
        # Test sorted approach
        result4 = solution.twoSum_sorted(nums[:], target)
        assert sorted(result4) == sorted(expected), f"Sorted failed: {result4}"
        print(f"  Sorted: {result4} ✓")
        
        print()
    
    print("All tests passed! ✨")


def mock_interview():
    """Simulate an interview scenario with follow-up questions"""
    print("=== Mock Interview: Two Sum ===\n")
    
    print("Interviewer: Can you solve the Two Sum problem?")
    print("Candidate: Sure! Let me start by clarifying the problem...")
    print()
    
    print("Initial Solution: Brute Force")
    print("Time: O(n²), Space: O(1)")
    solution = Solution()
    print("Code:", solution.twoSum_bruteforce.__doc__)
    print()
    
    print("Interviewer: Can you optimize it?")
    print("Candidate: Yes! We can use a hash table...")
    print("Optimized Solution: Hash Table")
    print("Time: O(n), Space: O(n)")
    print()
    
    print("Interviewer: What if the array was sorted?")
    print("Candidate: We could use two pointers for O(1) space...")
    print()
    
    print("Interviewer: What about handling duplicates?")
    print("Candidate: Our solution handles them correctly by checking indices...")
    print()
    
    print("=== Interview Complete ===")


if __name__ == "__main__":
    print("LeetCode #1: Two Sum\n")
    print("Testing all solutions...")
    print("-" * 40)
    test_solutions()
    print("-" * 40)
    print()
    mock_interview()