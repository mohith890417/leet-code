from math import comb
from typing import List


class Solution:

  def numOfWays(self, nums: List[int]) -> int:
    MOD = 10**9 + 7

    def dfs(arr: List[int]) -> int:
      if len(arr) <= 2:
        return 1

      root = arr[0]
      left_tree = [x for x in arr if x < root]
      right_tree = [x for x in arr if x > root]

      ways_left = dfs(left_tree)
      ways_right = dfs(right_tree)

      # Combinations: choose positions for left_tree elements in (left + right) slots
      combined_ways = comb(len(left_tree) + len(right_tree), len(left_tree))

      return (ways_left * ways_right * combined_ways) % MOD

    # Subtract 1 because the original array configuration itself shouldn't be counted as a "reordering"
    return (dfs(nums) - 1 + MOD) % MOD