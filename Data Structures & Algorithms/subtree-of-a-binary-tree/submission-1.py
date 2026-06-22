# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root_a: TreeNode, root_b: TreeNode) -> bool:
        if not root_a and not root_b:
            return True
        if not root_a or not root_b or root_a.val != root_b.val:
            return False
        return self.isSameTree(root_a.left, root_b.left) and self.isSameTree(root_a.right, root_b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)