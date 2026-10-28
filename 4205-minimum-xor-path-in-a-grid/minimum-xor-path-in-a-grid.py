class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR values to reach cell (i, j)
        dp = [set() for _ in range(n)]
        
        # Initialize the starting cell
        dp[0] = {grid[0][0]}
        
        for i in range(m):
            new_dp = [set() for _ in range(n)]
            for j in range(n):
                # Values from the top cell
                if i > 0:
                    for x in dp[j]:
                        new_dp[j].add(x ^ grid[i][j])
                # Values from the left cell
                if j > 0:
                    for x in new_dp[j - 1]:
                        new_dp[j].add(x ^ grid[i][j])
                
                # Base case for top-left cell
                if i == 0 and j == 0:
                    new_dp[0].add(grid[0][0])
                    
            dp = new_dp
            
        # The answer is the minimum value in the bottom-right cell's set
        return min(dp[n - 1])