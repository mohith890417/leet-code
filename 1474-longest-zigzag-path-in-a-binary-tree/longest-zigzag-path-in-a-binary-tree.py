# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def dfs(node, direction, length):
            if not node:
                return
            
            self.max_length = max(self.max_length, length)
            
            if direction == 'left':
                # If we came from left, next valid zigzag step is to go right (continue path)
                # and also restart a new path by going left from the current node.
                dfs(node.right, 'right', length + 1)
                dfs(node.left, 'left', 1)
            else:
                # If we came from right, next valid zigzag step is to go left (continue path)
                # and also restart a new path by going right from the current node.
                dfs(node.left, 'left', length + 1)
                dfs(node.right, 'right', 1)
        
        # Start DFS from the root with both potential initial directions and length 0
        dfs(root.left, 'left', 1)
        dfs(root.right, 'right', 1)
        
        return self.max_length