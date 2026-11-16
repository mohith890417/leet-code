class Solution:

    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp[i] represents the maximum money that can be robbed up to house i
        prev2 = 0  # max money up to i-2
        prev1 = 0  # max money up to i-1

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1