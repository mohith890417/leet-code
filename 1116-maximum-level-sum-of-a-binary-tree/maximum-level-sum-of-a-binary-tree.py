from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_sum = float('-inf')
        ans_level = 1
        current_level = 1
        
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update max_sum and ans_level if a strictly greater sum is found
            if level_sum > max_sum:
                max_sum = level_sum
                ans_level = current_level
                
            current_level += 1
            
        return ans_level