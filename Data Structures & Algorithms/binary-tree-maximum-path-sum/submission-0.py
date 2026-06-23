# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            res = max(res, node.val + max(0, left, right, left + right))
            return max(node.val, node.val + max(left, right))
            
        helper(root)
        return res