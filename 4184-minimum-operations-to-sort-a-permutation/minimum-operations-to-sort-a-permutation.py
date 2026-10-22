from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Helper function to check cyclic rotation shift
        def get_shift(arr, target):
            for shift in range(n):
                match = True
                for i in range(n):
                    if arr[(i + shift) % n] != target[i]:
                        match = False
                        break
                if match:
                    return shift
            return -1

        target_inc = list(range(n))
        target_dec = list(range(n))[::-1]

        # 1. Check if increasing rotation family
        pos_inc = get_shift(nums, target_inc)
        if pos_inc != -1:
            # Hint 1c: rotating left pos_inc times OR reverse -> rotate -> reverse
            # Reverse nums, find its shift to decreasing, then reverse back (+2 ops)
            rev_shift = get_shift(nums[::-1], target_dec)
            ans = pos_inc
            if rev_shift != -1:
                ans = min(ans, rev_shift + 2)
            return ans

        # 2. Check if decreasing rotation family
        pos_dec = get_shift(nums, target_dec)
        if pos_dec != -1:
            # Hint 1d: reverse first, or rotate first and then reverse
            return min(pos_dec + 1, (n - pos_dec) % n + 1)

        return -1      