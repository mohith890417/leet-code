class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute divisors for every possible substring length from 1 to n
        divs = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divs[length].append(d)
        
        # cost[i][j] = min changes to make substring s[i...j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                # Try all valid divisors d for the substring length
                for d in divs[length]:
                    current_cost = 0
                    # Check each of the d groups
                    for start in range(d):
                        group_chars = []
                        idx = i + start
                        while idx <= j:
                            group_chars.append(s[idx])
                            idx += d
                        
                        # Count mismatches to make this group a palindrome
                        left, right = 0, len(group_chars) - 1
                        while left < right:
                            if group_chars[left] != group_chars[right]:
                                current_cost += 1
                            left += 1
                            right -= 1
                    
                    min_changes = min(min_changes, current_cost)
                cost[i][j] = min_changes

        # dp[i][parts] = min changes to partition suffix s[i:] into 'parts' semi-palindromes
        memo = {}
        
        def dp(i: int, parts: int) -> int:
            if parts == 1:
                return cost[i][n - 1]
            if n - i < parts * 2:  # Minimum length of a semi-palindrome is 2
                return float('inf')
            if (i, parts) in memo:
                return memo[(i, parts)]
            
            res = float('inf')
            # Try every possible split point x for the first substring s[i...x]
            for x in range(i, n - parts + 1):
                res = min(res, cost[i][x] + dp(x + 1, parts - 1))
                
            memo[(i, parts)] = res
            return res

        return dp(0, k)