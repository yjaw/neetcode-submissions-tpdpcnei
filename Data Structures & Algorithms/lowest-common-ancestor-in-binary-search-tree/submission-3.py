# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, cur: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            return self.lowestCommonAncestor(cur, q, p)
        if not cur:
            return None
        if p.val <= cur.val <= q.val:
            return cur
        
        if p.val <= q.val < cur.val:
            return self.lowestCommonAncestor(cur.left, q, p)
        if cur.val < p.val <= q.val:
            return self.lowestCommonAncestor(cur.right, q, p) 