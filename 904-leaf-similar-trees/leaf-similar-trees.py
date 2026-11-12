# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            get_leaves(node.left, leaves)
            get_leaves(node.right, leaves)
            
        leaves1, leaves2 = [], []
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        
        return leaves1 == leaves2