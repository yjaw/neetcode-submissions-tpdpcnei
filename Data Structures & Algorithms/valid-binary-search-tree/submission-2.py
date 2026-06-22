# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node: Optional[TreeNode], lo: int, hi: int) -> bool:
        if not node:
            return True
        if lo < node.val < hi:
            return self.helper(node.left, lo, node.val) and self.helper(node.right, node.val, hi)
        else:
            return False
        
