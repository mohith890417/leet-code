class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros_count = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
                
            # If there are more than 1 zeros in the window, shrink from the left
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
                
            # The length of the window minus 1 (because we must delete one element)
            max_length = max(max_length, right - left)
            
        return max_length