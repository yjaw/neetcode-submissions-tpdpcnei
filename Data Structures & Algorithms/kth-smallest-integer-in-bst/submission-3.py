# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def helper(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if len(in_order) == k:
                return
            helper(node.left)
            in_order.append(node.val)
            helper(node.right)
            return
        
        helper(root)
        print(in_order)
        return in_order[k - 1]
        # T: O(N), S: O(H)