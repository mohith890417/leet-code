class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        max_factor = max(f for f, _ in items)

        factor_freq = [0] * (max_factor + 1)
        for f, _ in items:
            factor_freq[f] += 1

        first_gain = [0] * n
        for i, (f, _) in enumerate(items):
            multiples_of_f = 0
            for mult in range(f, max_factor + 1, f):
                multiples_of_f += factor_freq[mult]
            freebies = multiples_of_f - 1
            first_gain[i] = 1 + freebies

        dp = [0] * (budget + 1)

        # Step 1: First copy of each item (0/1 transition)
        for (_, price), gain in zip(items, first_gain):
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain > dp[b]:
                    dp[b] = dp[b - price] + gain

        # Step 2: Additional copies of any item (unbounded transition, +1 copy each)
        for _, price in items:
            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return max(dp)