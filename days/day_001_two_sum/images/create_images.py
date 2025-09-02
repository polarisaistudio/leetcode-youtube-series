#!/usr/bin/env python3
"""
Script to generate Two Sum visualization images programmatically.
Creates the PNG files referenced in the video scripts.

Requirements: pip install matplotlib pillow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_problem_example():
    """Create problem_example.png - Visual representation of the problem"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'Two Sum Problem Example', ha='center', va='center', 
            fontsize=20, fontweight='bold')
    
    # Array visualization
    array_values = [2, 7, 11, 15]
    array_indices = [0, 1, 2, 3]
    
    # Draw array boxes
    for i, (val, idx) in enumerate(zip(array_values, array_indices)):
        x = 1.5 + i * 2
        y = 5
        
        # Highlight the solution pair (indices 0 and 1)
        color = '#4CAF50' if i in [0, 1] else '#E0E0E0'
        edge_color = '#2E7D32' if i in [0, 1] else '#BDBDBD'
        
        # Value box
        rect = FancyBboxPatch((x-0.4, y-0.4), 0.8, 0.8, 
                             boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor=edge_color, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, str(val), ha='center', va='center', fontsize=16, fontweight='bold')
        
        # Index label
        ax.text(x, y-1, f'[{idx}]', ha='center', va='center', fontsize=14)
    
    # Target and equation
    ax.text(5, 3, 'Target: 9', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(5, 2.3, '2 + 7 = 9 ✓', ha='center', va='center', fontsize=14, color='#4CAF50')
    ax.text(5, 1.6, 'Return: [0, 1]', ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Arrow pointing to solution
    ax.annotate('', xy=(2.5, 4.5), xytext=(2.5, 3.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='#4CAF50'))
    ax.annotate('', xy=(4.5, 4.5), xytext=(4.5, 3.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='#4CAF50'))
    
    plt.tight_layout()
    plt.savefig('/Users/xinwang/projects/git/leetcode-youtube-series/days/day_001_two_sum/images/problem_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_complexity_comparison():
    """Create complexity_comparison.png - Performance comparison chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Comparison table
    ax1.axis('tight')
    ax1.axis('off')
    ax1.set_title('Approach Comparison', fontsize=16, fontweight='bold', pad=20)
    
    table_data = [
        ['Method', 'Time', 'Space', 'Description'],
        ['Brute Force', 'O(n²)', 'O(1)', 'Check all pairs'],
        ['Hash Table', 'O(n)', 'O(n)', 'Single pass lookup'],
        ['Two Pointers*', 'O(n log n)', 'O(1)', 'If array sorted']
    ]
    
    colors = [['#E0E0E0']*4, ['#FFCDD2']*4, ['#C8E6C9']*4, ['#DCEDC1']*4]
    
    table = ax1.table(cellText=table_data, cellColours=colors,
                     cellLoc='center', loc='center',
                     colWidths=[0.3, 0.2, 0.2, 0.3])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)
    
    # Growth comparison chart
    ax2.set_title('Time Complexity Growth', fontsize=16, fontweight='bold')
    
    n = np.array([100, 1000, 5000, 10000])
    brute_force = n ** 2 / 1000  # Scale for visibility
    hash_table = n
    
    ax2.plot(n, brute_force, 'r-o', label='Brute Force O(n²)', linewidth=2)
    ax2.plot(n, hash_table, 'g-o', label='Hash Table O(n)', linewidth=2)
    
    ax2.set_xlabel('Array Size (n)', fontsize=12)
    ax2.set_ylabel('Operations (scaled)', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/Users/xinwang/projects/git/leetcode-youtube-series/days/day_001_two_sum/images/complexity_comparison.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_hash_table_visualization():
    """Create hash_table_approach.png - Step-by-step hash table operations"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(7, 11.5, 'Hash Table Approach: Step by Step', ha='center', va='center',
            fontsize=18, fontweight='bold')
    
    # Array
    ax.text(1, 10, 'Array: [2, 7, 11, 15]', fontsize=14, fontweight='bold')
    ax.text(1, 9.5, 'Target: 9', fontsize=14, fontweight='bold')
    
    # Step 1
    step1_y = 8.5
    ax.text(1, step1_y, 'Step 1:', fontsize=14, fontweight='bold', color='#2196F3')
    ax.text(2.5, step1_y, 'i=0, num=2, complement=7', fontsize=12)
    ax.text(2.5, step1_y-0.4, 'seen = {}', fontsize=12, family='monospace')
    ax.text(2.5, step1_y-0.8, '7 not found → add to hash table', fontsize=12, color='#FF9800')
    ax.text(2.5, step1_y-1.2, 'seen = {2: 0}', fontsize=12, family='monospace', color='#4CAF50')
    
    # Step 2  
    step2_y = 6.5
    ax.text(1, step2_y, 'Step 2:', fontsize=14, fontweight='bold', color='#2196F3')
    ax.text(2.5, step2_y, 'i=1, num=7, complement=2', fontsize=12)
    ax.text(2.5, step2_y-0.4, 'seen = {2: 0}', fontsize=12, family='monospace')
    ax.text(2.5, step2_y-0.8, '2 FOUND! → return [0, 1]', fontsize=12, color='#4CAF50', fontweight='bold')
    
    # Visual hash table
    hash_x = 9
    ax.text(hash_x, 9, 'Hash Table Evolution:', fontsize=14, fontweight='bold')
    
    # Initial state
    rect1 = patches.Rectangle((hash_x, 7.8), 3, 0.8, linewidth=1, edgecolor='black', facecolor='#F5F5F5')
    ax.add_patch(rect1)
    ax.text(hash_x + 1.5, 8.2, 'Initial: {}', ha='center', va='center', fontsize=11)
    
    # After step 1
    rect2 = patches.Rectangle((hash_x, 6.8), 3, 0.8, linewidth=1, edgecolor='black', facecolor='#E3F2FD')
    ax.add_patch(rect2)
    ax.text(hash_x + 1.5, 7.2, 'After step 1: {2: 0}', ha='center', va='center', fontsize=11)
    
    # Result
    rect3 = patches.Rectangle((hash_x, 5.8), 3, 0.8, linewidth=2, edgecolor='#4CAF50', facecolor='#C8E6C9')
    ax.add_patch(rect3)
    ax.text(hash_x + 1.5, 6.2, 'Found match!', ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Result box
    result_rect = patches.FancyBboxPatch((5, 3), 4, 1.5, boxstyle="round,pad=0.2",
                                        facecolor='#4CAF50', edgecolor='#2E7D32', linewidth=3)
    ax.add_patch(result_rect)
    ax.text(7, 3.75, 'SOLUTION FOUND', ha='center', va='center', 
            fontsize=16, fontweight='bold', color='white')
    ax.text(7, 3.25, 'Return: [0, 1]', ha='center', va='center',
            fontsize=14, color='white')
    
    plt.tight_layout()
    plt.savefig('/Users/xinwang/projects/git/leetcode-youtube-series/days/day_001_two_sum/images/hash_table_approach.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_brute_force_visualization():
    """Create brute_force_approach.png - Nested loop visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(6, 11.5, 'Brute Force Approach: All Pair Comparisons', ha='center', va='center',
            fontsize=16, fontweight='bold')
    
    # Array representation
    ax.text(6, 10.5, 'Array: [2, 7, 11, 15]  Target: 9', ha='center', va='center', fontsize=14)
    
    # Comparison table
    comparisons = [
        ('i=0, j=1', '2 + 7 = 9', '✓ FOUND!', '#4CAF50'),
        ('i=0, j=2', '2 + 11 = 13', '✗', '#F44336'),
        ('i=0, j=3', '2 + 15 = 17', '✗', '#F44336'),
        ('i=1, j=2', '7 + 11 = 18', '✗', '#F44336'),
        ('i=1, j=3', '7 + 15 = 22', '✗', '#F44336'),
        ('i=2, j=3', '11 + 15 = 26', '✗', '#F44336'),
    ]
    
    y_start = 9
    for i, (indices, calculation, result, color) in enumerate(comparisons):
        y = y_start - i * 0.8
        
        # Background color for found solution
        if '✓' in result:
            bg_rect = patches.Rectangle((1, y-0.3), 10, 0.6, 
                                      facecolor='#C8E6C9', alpha=0.5)
            ax.add_patch(bg_rect)
        
        ax.text(1.5, y, indices, fontsize=12, fontweight='bold')
        ax.text(4, y, calculation, fontsize=12, family='monospace')
        ax.text(8, y, result, fontsize=12, fontweight='bold', color=color)
    
    # Summary
    ax.text(6, 3.5, 'Total Comparisons: 6 (n×(n-1)/2 where n=4)', 
            ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(6, 3, 'Time Complexity: O(n²)', ha='center', va='center', fontsize=14, color='#F44336')
    ax.text(6, 2.5, 'Space Complexity: O(1)', ha='center', va='center', fontsize=14, color='#4CAF50')
    
    plt.tight_layout()
    plt.savefig('/Users/xinwang/projects/git/leetcode-youtube-series/days/day_001_two_sum/images/brute_force_approach.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_algorithm_flowchart():
    """Create algorithm_flowchart.png - Decision flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Title
    ax.text(5, 13.5, 'Two Sum: Algorithm Selection Guide', ha='center', va='center',
            fontsize=16, fontweight='bold')
    
    # Decision nodes
    nodes = [
        (5, 12, 'Given: Array + Target', '#E3F2FD', 'rect'),
        (5, 10.5, 'Memory constrained?', '#FFF3E0', 'diamond'),
        (2, 9, 'Use Brute Force\nO(n²) time, O(1) space', '#FFCDD2', 'rect'),
        (8, 9, 'Array sorted?', '#FFF3E0', 'diamond'),
        (6.5, 7.5, 'Use Two Pointers\nO(n) time, O(1) space', '#DCEDC1', 'rect'),
        (8, 7.5, 'Use Hash Table\nO(n) time, O(n) space', '#C8E6C9', 'rect'),
    ]
    
    for x, y, text, color, shape in nodes:
        if shape == 'diamond':
            # Diamond shape for decision nodes
            diamond = patches.RegularPolygon((x, y), 4, radius=0.8, 
                                           orientation=np.pi/4, 
                                           facecolor=color, edgecolor='black')
            ax.add_patch(diamond)
        else:
            # Rectangle for process nodes
            rect = patches.FancyBboxPatch((x-1, y-0.4), 2, 0.8, 
                                        boxstyle="round,pad=0.1",
                                        facecolor=color, edgecolor='black')
            ax.add_patch(rect)
        
        ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Arrows with labels
    arrows = [
        ((5, 11.7), (5, 11.3), ''),
        ((4.2, 10.2), (2.8, 9.3), 'YES'),
        ((5.8, 10.2), (7.2, 9.3), 'NO'),
        ((7.2, 8.7), (7.2, 8.3), 'YES'),
        ((8.8, 8.7), (8, 8.3), 'NO'),
    ]
    
    for start, end, label in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
        if label:
            mid_x, mid_y = (start[0] + end[0])/2, (start[1] + end[1])/2
            ax.text(mid_x + 0.2, mid_y + 0.1, label, fontsize=9, 
                   fontweight='bold', color='blue')
    
    # Interview tips
    ax.text(5, 5.5, 'Interview Tips:', ha='center', va='center', 
            fontsize=14, fontweight='bold', color='#1976D2')
    
    tips = [
        '• Start with clarifying questions',
        '• Implement brute force first',
        '• Discuss trade-offs explicitly', 
        '• Optimize based on constraints',
        '• Test with edge cases'
    ]
    
    for i, tip in enumerate(tips):
        ax.text(1, 4.8 - i*0.4, tip, fontsize=11, va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/xinwang/projects/git/leetcode-youtube-series/days/day_001_two_sum/images/algorithm_flowchart.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def main():
    """Generate all Two Sum visualization images"""
    print("🎨 Generating Two Sum visualization images...")
    
    try:
        create_problem_example()
        print("✅ Created problem_example.png")
        
        create_brute_force_visualization()
        print("✅ Created brute_force_approach.png")
        
        create_hash_table_visualization()
        print("✅ Created hash_table_approach.png")
        
        create_complexity_comparison()
        print("✅ Created complexity_comparison.png")
        
        create_algorithm_flowchart()
        print("✅ Created algorithm_flowchart.png")
        
        print("\n🚀 All images generated successfully!")
        print("📁 Images saved to: days/day_001_two_sum/images/")
        
    except ImportError as e:
        print(f"❌ Missing required packages: {e}")
        print("Install with: pip install matplotlib pillow")
    except Exception as e:
        print(f"❌ Error generating images: {e}")

if __name__ == "__main__":
    main()