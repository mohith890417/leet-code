from typing import List


class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        def is_rotation(a, b):
            k = len(a)

            if k == 0:
                return True

            # Build the KMP prefix table for b
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]

                if b[i] == b[j]:
                    j += 1

                lps[i] = j

            # Search for b inside the cyclic sequence a + a
            j = 0

            for i in range(2 * k - 1):
                value = a[i % k]

                while j > 0 and value != b[j]:
                    j = lps[j - 1]

                if value == b[j]:
                    j += 1

                if j == k:
                    return True

            return False

        # Find divisors of n
        divisors = []
        i = 1

        while i * i <= n:
            if n % i == 0:
                divisors.append(i)

                if i * i != n:
                    divisors.append(n // i)

            i += 1

        ans = 0

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                expected = target[start:start + k]

                if not is_rotation(block, expected):
                    valid = False
                    break

            if valid:
                ans += k

        return ans