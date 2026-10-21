class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    # Step 1: Calculate left/prefix products
    left_product = 1
    for i in range(n):
      answer[i] = left_product
      left_product *= nums[i]

    # Step 2: Calculate right/suffix products and multiply with prefix products
    right_product = 1
    for i in range(n - 1, -1, -1):
      answer[i] *= right_product
      right_product *= nums[i]

    return answer