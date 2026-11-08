from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Count the frequency of each row
        row_counts = Counter(tuple(row) for row in grid)
        
        # Count the frequency of each column
        col_counts = Counter(tuple(grid[r][c] for r in range(n)) for c in range(n))
        
        # Calculate matching pairs
        ans = 0
        for row, count in row_counts.items():
            if row in col_counts:
                ans += count * col_counts[row]
                
        etur = ans # Just to match standard return
        return ans