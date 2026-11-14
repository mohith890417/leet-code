from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        minutes_elapsed = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Run BFS level by level (minute by minute)
        while queue:
            r, c, minutes = queue.popleft()
            minutes_elapsed = max(minutes_elapsed, minutes)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # If adjacent cell has a fresh orange, rot it and add to queue
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, minutes + 1))
                    
        # Step 3: Check if any fresh oranges are left
        return minutes_elapsed if fresh_count == 0 else -1