class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        
        # Elements in set1 that are not in set2, and vice versa
        return [list(set1 - set2), list(set2 - set1)]
        