# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        i = inorder.index(val)

        cur = TreeNode(val = val)
        cur.left = self.buildTree(preorder[1: 1 + i], inorder[: i])
        cur.right = self.buildTree(preorder[1 + i: ], inorder[i + 1: ])
        return cur
