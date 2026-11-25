from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        # Double rolling hash to keep collision probability negligible
        base1, mod1 = 100003, 1_000_000_007
        base2, mod2 = 100019, 1_000_000_009

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            val = nums[i]
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + val) % mod1
            h2[i + 1] = (h2[i] * base2 + val) % mod2

        def sub_hash(left: int, right: int) -> tuple[int, int]:
            length = right - left
            res1 = (h1[right] - h1[left] * p1[length]) % mod1
            res2 = (h2[right] - h2[left] * p2[length]) % mod2
            return (res1, res2)

        def has_unique_of_length(length: int) -> bool:
            counts = Counter()
            for start in range(n - length + 1):
                counts[sub_hash(start, start + length)] += 1
            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        