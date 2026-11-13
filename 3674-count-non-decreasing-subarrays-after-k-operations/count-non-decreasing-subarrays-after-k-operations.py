
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Next strictly greater element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Binary lifting tables
        LOG = n.bit_length()
        jump = [[n] * (n + 1) for _ in range(LOG)]
        total = [[0] * (n + 1) for _ in range(LOG)]

        for i in range(n):
            jump[0][i] = nxt[i]
            total[0][i] = nums[i] * (nxt[i] - i)

        for p in range(1, LOG):
            for i in range(n):
                mid = jump[p - 1][i]
                jump[p][i] = jump[p - 1][mid]
                total[p][i] = (
                    total[p - 1][i] + total[p - 1][mid]
                )

        # Sum of prefix maximums in nums[l:r+1]
        def prefix_max_sum(l, r):
            pos = l
            result = 0

            for p in range(LOG - 1, -1, -1):
                nxt_pos = jump[p][pos]

                if nxt_pos <= r + 1:
                    result += total[p][pos]
                    pos = nxt_pos

            if pos <= r:
                result += nums[pos] * (r - pos + 1)

            return result

        # Sliding window
        ans = 0
        left = 0

        for right in range(n):
            while left <= right:
                cost = (
                    prefix_max_sum(left, right)
                    - (prefix[right + 1] - prefix[left])
                )

                if cost <= k:
                    break

                left += 1

            ans += right - left + 1

        return ans
