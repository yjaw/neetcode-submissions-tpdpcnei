# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(cur: int, node: TreeNode) -> int:
            if not node:
                return 0
            
            count = 1 if node.val >= cur else 0
            cur = max(cur, node.val)
            return count + check(cur, node.left) + check(cur, node.right)
        
        if not root:
            return 0
        return check(root.val, root)
            
