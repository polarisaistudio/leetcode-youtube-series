# Day 1: Two Sum - Mermaid Visualizations

## 1. Problem Overview

```mermaid
graph LR
    subgraph "Input"
        A[Array: 2,7,11,15]
        B[Target: 9]
    end
    
    subgraph "Process"
        C[Find two indices]
        D[nums_i + nums_j = target]
    end
    
    subgraph "Output"
        E[Return: 0,1]
        F[Because: 2+7=9]
    end
    
    A --> C
    B --> C
    C --> D
    D --> E
    D --> F
    
    style A fill:#E3F2FD
    style B fill:#E3F2FD
    style E fill:#C8E6C9
    style F fill:#C8E6C9
```

## 2. Brute Force Approach

```mermaid
flowchart TB
    Start([Start]) --> Init[Initialize i = 0]
    Init --> OuterLoop{i < n?}
    OuterLoop -->|Yes| InitJ[j = i + 1]
    OuterLoop -->|No| NotFound[Return empty]
    
    InitJ --> InnerLoop{j < n?}
    InnerLoop -->|Yes| Check{nums_i + nums_j == target?}
    InnerLoop -->|No| IncI[i++]
    
    Check -->|Yes| Found[Return i, j]
    Check -->|No| IncJ[j++]
    
    IncJ --> InnerLoop
    IncI --> OuterLoop
    
    Found --> End([End])
    NotFound --> End
    
    style Start fill:#E3F2FD
    style Found fill:#C8E6C9
    style NotFound fill:#FFCDD2
    style End fill:#E0E0E0
```

### Brute Force Complexity

```mermaid
graph TD
    subgraph "Time Complexity: O(n²)"
        T1[First Loop: n iterations]
        T2[Nested Loop: n-1, n-2, ..., 1]
        T3[Total: n*n-1/2 = O n²]
        T1 --> T2 --> T3
    end
    
    subgraph "Space Complexity: O(1)"
        S1[Only loop variables]
        S2[Constant extra space]
        S1 --> S2
    end
    
    style T3 fill:#FFCDD2
    style S2 fill:#C8E6C9
```

## 3. Hash Table Approach

```mermaid
flowchart TB
    Start([Start]) --> Init[Initialize empty hash table]
    Init --> Loop{For each num in array}
    
    Loop -->|Yes| Calc[Calculate complement = target - num]
    Calc --> CheckHash{complement in hash table?}
    
    CheckHash -->|Yes| Found[Return hash_complement, current_index]
    CheckHash -->|No| Store[Store num: index in hash table]
    
    Store --> Next[Move to next element]
    Next --> Loop
    
    Loop -->|No more elements| NotFound[Return empty]
    
    Found --> End([End])
    NotFound --> End
    
    style Start fill:#E3F2FD
    style Found fill:#C8E6C9
    style Init fill:#FFF3E0
    style End fill:#E0E0E0
```

### Hash Table Step-by-Step Example

```mermaid
graph TD
    subgraph "Step 1: num=2, index=0"
        A1[Complement = 9-2 = 7]
        A2[Hash table: empty]
        A3[7 not found]
        A4[Add 2:0 to hash]
        A1 --> A2 --> A3 --> A4
    end
    
    subgraph "Step 2: num=7, index=1"
        B1[Complement = 9-7 = 2]
        B2["Hash table: {2:0}"]
        B3[2 FOUND!]
        B4["Return [0,1]"]
        B1 --> B2 --> B3 --> B4
    end
    
    A4 --> B1
    
    style B3 fill:#C8E6C9
    style B4 fill:#C8E6C9
```

## 4. Algorithm Selection Flowchart

```mermaid
flowchart TD
    Start([Given: Array + Target]) --> Q1{Memory Constrained?}
    
    Q1 -->|Yes| BF[Use Brute Force<br/>Time: O n²<br/>Space: O 1]
    Q1 -->|No| Q2{Array Sorted?}
    
    Q2 -->|Yes| TP[Use Two Pointers<br/>Time: O n<br/>Space: O 1]
    Q2 -->|No| HT[Use Hash Table<br/>Time: O n<br/>Space: O n]
    
    BF --> End([Implement Solution])
    TP --> End
    HT --> End
    
    style Start fill:#E3F2FD
    style BF fill:#FFCDD2
    style TP fill:#DCEDC1
    style HT fill:#C8E6C9
    style End fill:#E0E0E0
```

## 5. Complexity Comparison

```mermaid
graph LR
    subgraph "Brute Force"
        BF1[Time: O n²]
        BF2[Space: O 1]
        BF3[When: Memory critical]
    end
    
    subgraph "Hash Table"
        HT1[Time: O n]
        HT2[Space: O n]
        HT3[When: Speed critical]
    end
    
    subgraph "Two Pointers"
        TP1[Time: O n]
        TP2[Space: O 1]
        TP3[When: Array sorted]
    end
    
    style BF1 fill:#FFCDD2
    style HT1 fill:#C8E6C9
    style TP1 fill:#C8E6C9
    style BF2 fill:#C8E6C9
    style HT2 fill:#FFCDD2
    style TP2 fill:#C8E6C9
```

## 6. Interview Communication Flow

```mermaid
sequenceDiagram
    participant I as Interviewer
    participant C as Candidate
    
    I->>C: Solve Two Sum problem
    C->>I: Clarify requirements
    Note over C: Can array be empty?<br/>Return indices or values?<br/>Multiple solutions?
    
    I->>C: Clarifications provided
    C->>I: Present brute force O(n²)
    Note over C: Implement nested loops
    
    I->>C: Can you optimize?
    C->>I: Yes, using hash table O(n)
    Note over C: Trade space for time
    
    I->>C: What if sorted?
    C->>I: Two pointers O(n), O(1) space
    Note over C: Discuss trade-offs
    
    I->>C: Test your solution
    C->>I: Walk through examples
    Note over C: Edge cases included
```

## 7. Test Cases Coverage

```mermaid
mindmap
  root((Test Cases))
    Basic
      [2,7,11,15], target=9
      [3,2,4], target=6
    Edge Cases
      Duplicates
        [3,3], target=6
      Negatives
        [-1,-2,-3,-4,-5], target=-8
      Zeros
        [0,4,3,0], target=0
      Min Size
        [1,2], target=3
    Boundaries
      Large Numbers
        [10^9, -10^9], target=0
      Large Array
        10,000 elements
```

## 8. Pattern Recognition

```mermaid
graph TD
    TwoSum[Two Sum<br/>Foundation Problem]
    
    TwoSum --> Patterns{Key Patterns}
    
    Patterns --> P1[Complement Search<br/>target - current]
    Patterns --> P2[Hash Table Lookup<br/>O 1 average]
    Patterns --> P3[Two Pointers<br/>For sorted arrays]
    Patterns --> P4[Space-Time Tradeoff<br/>Memory vs Speed]
    
    P1 --> App1[3Sum Problem]
    P2 --> App2[Subarray Sum]
    P3 --> App3[Container Water]
    P4 --> App4[Dynamic Programming]
    
    style TwoSum fill:#E3F2FD
    style P1 fill:#FFF3E0
    style P2 fill:#FFF3E0
    style P3 fill:#FFF3E0
    style P4 fill:#FFF3E0
```

## Rendering Instructions

### For GitHub
GitHub automatically renders Mermaid diagrams in markdown files.

### For Local Development
1. **VS Code**: Install "Markdown Preview Mermaid Support" extension
2. **Command Line**: Use `mermaid-cli` to generate images:
   ```bash
   npm install -g @mermaid-js/mermaid-cli
   mmdc -i diagrams.md -o output.png
   ```

### For Blog Posts
1. **Medium**: Use mermaid.live to generate SVG/PNG
2. **Dev.to**: Supports Mermaid natively
3. **Personal Blog**: Include mermaid.js library

### For Videos
1. Use mermaid.live to export as PNG/SVG
2. Import into video editing software
3. Or screen record the live rendering

## Color Scheme Reference
- `#E3F2FD` - Light Blue (Input/Start)
- `#C8E6C9` - Light Green (Success/Optimal)
- `#FFCDD2` - Light Red (Inefficient/Error)
- `#FFF3E0` - Light Orange (Process/Warning)
- `#E0E0E0` - Light Gray (Neutral/End)
- `#DCEDC1` - Light Lime (Alternative)