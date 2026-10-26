from collections import deque
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False * n for _ in range(n)] for _ in range(m)]
        # Alternatively, you can modify grid values in-place to save space (e.g., grid[r][c] = 0)
        
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    # Start BFS for a new island
                    island_sum = 0
                    queue = deque([(r, c)])
                    visited[r][c] = True
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        island_sum += grid[curr_r][curr_c]
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                    
                    # Check if the total value of the island is divisible by k
                    if island_sum % k == 0:
                        count += 1
                        
        return count