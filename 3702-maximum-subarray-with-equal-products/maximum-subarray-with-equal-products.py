import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            cur_gcd = 0
            cur_lcm = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                cur_gcd = x if cur_gcd == 0 else math.gcd(cur_gcd, x)
                cur_lcm = math.lcm(cur_lcm, x)

                if prod == cur_lcm * cur_gcd:
                    ans = max(ans, j - i + 1)

        return ans