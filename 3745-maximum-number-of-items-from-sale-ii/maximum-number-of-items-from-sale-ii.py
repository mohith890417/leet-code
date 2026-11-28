
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        divisible_count = [0] * (n + 1)

        for factor in range(1, n + 1):
            for multiple in range(factor, n + 1, factor):
                divisible_count[factor] += freq[multiple]

        candidates = []

        for factor, price in items:
            free_count = divisible_count[factor] - 1

            if free_count > 0 and price < 2 * min_price:
                candidates.append((price, free_count))

        candidates.sort()

        answer = 0
        remaining = budget

        for price, free_count in candidates:
            if remaining < price:
                break

            copies = min(free_count, remaining // price)

            answer += 2 * copies
            remaining -= copies * price

            if copies < free_count:
                break

        answer += remaining // min_price

        return answer
