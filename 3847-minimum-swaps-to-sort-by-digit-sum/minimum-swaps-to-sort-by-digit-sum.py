class Solution:

  def minSwaps(self, nums: list[int]) -> int:
    n = len(nums)

    def digit_sum(x):
      s = 0
      while x > 0:
        s += x % 10
        x //= 10
      return s

    # Pair each number with (digit_sum, value, original_index)
    arr = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]

    # Sort based on digit sum, then value
    arr.sort(key=lambda x: (x[0], x[1]))

    # Find the number of cycles in the permutation
    visited = [False] * n
    swaps = 0

    for i in range(n):
      if visited[i] or arr[i][2] == i:
        continue

      # Traverse the cycle
      cycle_size = 0
      curr = i
      while not visited[curr]:
        visited[curr] = True
        curr = arr[curr][2]
        cycle_size += 1

      if cycle_size > 1:
        swaps += cycle_size - 1

    return swaps
        