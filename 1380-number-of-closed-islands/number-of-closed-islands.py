class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Out of bounds or water cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            # Mark the current land as visited/water
            grid[r][c] = 1
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Eliminate all land cells connected to the top and bottom borders
        for c in range(cols):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[rows - 1][c] == 0:
                dfs(rows - 1, c)

        # 2. Eliminate all land cells connected to the left and right borders
        for r in range(rows):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][cols - 1] == 0:
                dfs(r, cols - 1)

        # 3. Count remaining disconnected closed islands in the interior
        closed_islands_count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    dfs(r, c)  # Sink the entire closed island

        return closed_islands_count