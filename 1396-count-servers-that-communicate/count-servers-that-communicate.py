class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Step 1: Count the number of servers in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        # Step 2: Count servers that are part of a row or column with > 1 server
        communicating_servers = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        T = communicating_servers
        return T