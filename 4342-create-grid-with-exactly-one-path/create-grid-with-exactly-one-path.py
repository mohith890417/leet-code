class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Initialize an m x n grid filled with obstacles ('#')
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Make the top row entirely free cells ('.' )
        for j in range(n):
            grid[0][j] = '.'
            
        # Make the last column entirely free cells ('.' )
        for i in range(m):
            grid[i][n - 1] = '.'
            
        # Convert each row list into a string
        return ["".join(row) for row in grid]