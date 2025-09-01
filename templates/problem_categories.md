# LeetCode Problem Categories & Patterns

## 1. Arrays & Strings

### Basic Patterns
- Two Pointers
- Sliding Window
- Prefix Sum
- Kadane's Algorithm
- Dutch National Flag

### Key Problems
- Two Sum variants
- Subarray problems
- Rotation problems
- Matrix manipulation
- String matching

### Interview Tips
- Always consider sorting first
- Hash tables for O(1) lookup
- Watch for integer overflow
- Handle empty arrays/strings

## 2. Linked Lists

### Operations
- Reversal (iterative/recursive)
- Merge/Split
- Cycle detection (Floyd's)
- Finding middle
- Remove/Insert nodes

### Common Patterns
- Dummy head technique
- Fast/Slow pointers
- Previous pointer tracking
- In-place modifications

## 3. Trees

### Traversals
- Preorder (Root-Left-Right)
- Inorder (Left-Root-Right)
- Postorder (Left-Right-Root)
- Level-order (BFS)

### Patterns
- Recursion vs Iteration
- Top-down vs Bottom-up
- Path problems
- Subtree problems
- Ancestor problems

## 4. Graphs

### Representations
- Adjacency List
- Adjacency Matrix
- Edge List

### Algorithms
- DFS (stack/recursion)
- BFS (queue)
- Topological Sort
- Dijkstra's
- Union Find
- Minimum Spanning Tree

## 5. Dynamic Programming

### Categories
1. **Linear DP**: Single array/sequence
2. **Grid DP**: 2D problems
3. **Interval DP**: Substring/subarray
4. **Tree DP**: On tree structures
5. **State Machine DP**: Multiple states

### Approach
1. Define state
2. Write recurrence relation
3. Identify base cases
4. Optimize space if possible

## 6. Binary Search

### Templates
```python
# Template 1: Find exact value
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Template 2: Find first true
left, right = 0, len(arr)
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
```

## 7. Backtracking

### Template
```python
def backtrack(path, choices):
    if goal_reached:
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, new_choices)
            path.pop()  # backtrack
```

### Problems
- Permutations
- Combinations
- Subsets
- N-Queens
- Sudoku

## 8. Greedy

### Characteristics
- Local optimal → Global optimal
- No backtracking needed
- Proof of correctness important

### Classic Problems
- Activity Selection
- Huffman Coding
- Interval Scheduling
- Jump Game
- Gas Station

## 9. Heap/Priority Queue

### Operations
- Insert: O(log n)
- Extract max/min: O(log n)
- Peek: O(1)

### Use Cases
- K largest/smallest
- Median finding
- Merge K sorted
- Meeting rooms
- Task scheduling

## 10. Trie

### Structure
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

### Applications
- Autocomplete
- Spell checker
- Word search
- Prefix matching

## 11. Union Find

### Operations
- Find(x): Find root
- Union(x, y): Merge sets
- Path compression
- Union by rank

### Problems
- Connected components
- Cycle detection
- MST (Kruskal's)
- Account merge

## 12. Bit Manipulation

### Operations
- AND (&), OR (|), XOR (^)
- NOT (~), Left shift (<<), Right shift (>>)

### Tricks
```python
# Check if power of 2
n & (n - 1) == 0

# Get rightmost set bit
n & -n

# Clear rightmost set bit
n & (n - 1)

# XOR properties
a ^ a = 0
a ^ 0 = a
```

## 13. Design Problems

### Components
- Data structures choice
- API design
- Scalability
- Trade-offs

### Examples
- LRU/LFU Cache
- Data structures (Stack, Queue)
- Iterator design
- System components

## 14. Math & Geometry

### Common Concepts
- GCD/LCM
- Prime numbers
- Modular arithmetic
- Combinatorics
- Coordinate geometry

### Algorithms
- Sieve of Eratosthenes
- Euclidean algorithm
- Fast exponentiation
- Line intersection

## Pattern Recognition Guide

### When to use what?

**Two Pointers**
- Sorted array/list
- Palindrome checking
- Pair/triplet finding

**Sliding Window**
- Substring/subarray
- Fixed or variable size
- Optimization problems

**Hash Table**
- Frequency counting
- Pair finding
- Caching/memoization

**Stack**
- Matching parentheses
- Monotonic problems
- Expression evaluation

**BFS**
- Shortest path (unweighted)
- Level-order traversal
- Connected components

**DFS**
- All paths
- Cycle detection
- Topological sort

**Binary Search**
- Sorted data
- Search space reduction
- Optimization problems

**Dynamic Programming**
- Optimal substructure
- Overlapping subproblems
- Count ways/paths

**Greedy**
- Choice property
- No future dependence
- Sorting often helps

**Union Find**
- Disjoint sets
- Connected components
- Cycle in undirected graph