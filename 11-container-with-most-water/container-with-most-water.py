class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width between the two pointers
            width = right - left
            
            # The height is constrained by the shorter of the two lines
            current_height = min(height[left], height[right])
            
            # Calculate current area and update max_water
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water