class Solution:

    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Helper to simulate the exact landing spot given starting cell and direction
        # dir: 0 for moving right, 1 for moving down
        def get_jump(r, c, d):
            curr_r, curr_c, curr_d = r, c, d
            while True:
                if grid[curr_r][curr_c] == 1:
                    # Hit a mirror, change direction
                    if curr_d == 0:  # was moving right -> turn down
                        curr_d = 1
                        curr_r += 1
                    else:  # was moving down -> turn right
                        curr_d = 0
                        curr_c += 1

                    # Check out of bounds
                    if not (0 <= curr_r < m and 0 <= curr_c < n):
                        return None
                else:
                    return (curr_r, curr_c, curr_d)

        # dp[i][j][d]: number of ways to be at (i, j) with direction d (0: right, 1: down)
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]

        # Base initial moves from (0, 0)
        # From (0,0), trying to go right means target is (0,1), down means (1,0)
        MOD = 10**9 + 7

        # Let's initialize DP by simulating initial steps from (0,0)
        for d, (nr, nc) in enumerate([(0, 1), (1, 0)]):
            if 0 <= nr < m and 0 <= nc < n:
                res = get_jump(nr, nc, d)
                if res:
                    tr, tc, td = res
                    dp[tr][tc][td] = (dp[tr][tc][td] + 1) % MOD

        # If start cell itself is a mirror or immediate moves are invalid, handle carefully.
        # Actually, grid[0][0] == 0 is guaranteed by constraints.

        for i in range(m):
            for j in range(n):
                for d in range(2):
                    ways = dp[i][j][d]
                    if ways == 0:
                        if i == 0 and j == 0:
                            pass  # handled via initial moves
                        else:
                            continue

                    if i == m - 1 and j == n - 1:
                        continue

                    # From (i, j), we can choose to move either Right (d=0) or Down (d=1) next
                    next_moves = []
                    if j + 1 < n:
                        next_moves.append((i, j + 1, 0))
                    if i + 1 < m:
                        next_moves.append((i + 1, j, 1))

                    for nr, nc, nd in next_moves:
                        res = get_jump(nr, nc, nd)
                        if res:
                            tr, tc, td = res
                            dp[tr][tc][td] = (dp[tr][tc][td] + ways) % MOD

        # Result is sum of ways arriving at the bottom-right corner (m-1, n-1)
        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD