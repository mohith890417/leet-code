class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = {}
        operations = 0
        
        for num in nums:
            complement = k - num
            # If the complement exists and has available counts, we found a pair
            if count.get(complement, 0) > 0:
                operations += 1
                count[complement] -= 1
            else:
                # Otherwise, increment the count of the current number
                count[num] = count.get(num, 0) + 1
                
        return operations