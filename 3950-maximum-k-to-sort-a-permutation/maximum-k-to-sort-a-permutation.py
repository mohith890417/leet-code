class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1  # Using -1 or a bitmask with all bits set (like (1 << 20) - 1 depending on constraints)
        
        # Alternatively, find the bitwise AND of all nums[i] != i
        misplaced = [nums[i] for i in range(len(nums)) if nums[i] != i]
        
        if not misplaced:
            return 0
            
        res = misplaced[0]
        for x in misplaced[1:]:
            res &= x
            
        return res