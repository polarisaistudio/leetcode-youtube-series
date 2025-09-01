# Day 1: Two Sum - Illustration Descriptions

## Illustration 1: Problem Example (illustration_1_two_sum_example.png)

### Visual Layout:
```
Input Array: [2, 7, 11, 15]
Indices:      0  1   2   3

Target: 9

Step-by-step visualization:
1. Check 2 (index 0): Need 9 - 2 = 7
2. Check 7 (index 1): Found! 2 + 7 = 9
3. Return indices: [0, 1]

Output: [0, 1]
```

### Design Elements:
- Array boxes with values inside
- Index numbers below each box
- Highlight the two numbers that sum to target (green)
- Arrow showing the addition: 2 + 7 = 9
- Clean, minimalist design with good contrast

## Illustration 2: Brute Force Approach (illustration_2_brute_force.png)

### Visual Layout:
```
Array: [2, 7, 11, 15]

Nested Loop Visualization:
i=0 → j=1: 2+7=9 ✓ Found!
i=0 → j=2: 2+11=13 
i=0 → j=3: 2+15=17
i=1 → j=2: 7+11=18
i=1 → j=3: 7+15=22
i=2 → j=3: 11+15=26

Time Complexity: O(n²)
```

### Design Elements:
- Show nested loop structure with arrows
- Color code: Current pair (blue), Found (green), Not match (gray)
- Include loop indices i and j
- Visualize all comparisons being made

## Illustration 3: Hash Table Approach (illustration_3_hash_table.png)

### Visual Layout:
```
Array: [2, 7, 11, 15]    Target: 9

Step 1: num=2, need=7
Hash Table: {2: 0}
7 not found → continue

Step 2: num=7, need=2
Hash Table: {2: 0}
2 found! → return [0, 1]

Time Complexity: O(n)
```

### Design Elements:
- Show array traversal with current pointer
- Hash table visualization as key-value pairs
- Complement calculation shown
- Step-by-step progression
- Success indicator when match found

## Illustration 4: Complexity Comparison (illustration_4_complexity_comparison.png)

### Visual Layout:
```
Comparison Chart:

Method        | Time    | Space  | Description
-------------|---------|--------|------------------
Brute Force  | O(n²)   | O(1)   | Check all pairs
Hash Table   | O(n)    | O(n)   | Single pass
Two Pointers | O(nlogn)| O(1)   | If sorted

Graph showing time growth:
[Line graph with n on x-axis, time on y-axis]
- Quadratic curve for O(n²)
- Linear line for O(n)
- Highlight crossover points
```

### Design Elements:
- Clean comparison table
- Growth rate visualization
- Color coding: Brute Force (red), Hash Table (green), Two Pointers (blue)
- Include practical implications (array size examples)

## Illustration 5: Edge Cases (illustration_5_edge_cases.png)

### Visual Layout:
```
Edge Case Examples:

1. Duplicate Values:
   [3, 3] target=6 → [0, 1] ✓

2. Negative Numbers:
   [-1, -2, -3, -4, -5] target=-8 → [2, 4] ✓

3. Zero Values:
   [0, 4, 3, 0] target=0 → [0, 3] ✓

4. Large Numbers:
   [1000000, 999999, 1] target=1000001 → [0, 2] ✓
```

### Design Elements:
- Multiple small examples
- Highlight special cases
- Show correct handling
- Use warning icons for common mistakes

## Animation Suggestions (for video):

1. **Array Traversal Animation**: 
   - Pointer moving through array
   - Hash table growing as elements are added
   - Highlight when match is found

2. **Comparison Animation**:
   - Show pairs being checked in brute force
   - Visualize O(n²) vs O(n) operations

3. **Hash Table Lookup**:
   - Animate the lookup process
   - Show O(1) access time

## Color Palette:
- Primary (Success): #4CAF50
- Secondary (Active): #2196F3
- Warning: #FF9800
- Error: #F44336
- Neutral: #9E9E9E
- Background: #1E1E1E
- Text: #FFFFFF