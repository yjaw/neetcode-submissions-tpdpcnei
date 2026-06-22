# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, cur: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not cur:
            return None
        if cur.val == p.val or cur.val == q.val:
            return cur
        
        left = self.lowestCommonAncestor(cur.left, p, q)
        right = self.lowestCommonAncestor(cur.right, p, q)
        if left and right:
            return cur
        return left if left else right

        # T: O(N), S: O(H)