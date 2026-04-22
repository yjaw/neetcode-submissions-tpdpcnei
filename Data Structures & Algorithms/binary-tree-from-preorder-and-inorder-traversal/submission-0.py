# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        
        cur_value = preorder[0]
        node = TreeNode(cur_value)
        index = inorder.index(cur_value)
        node.left = self.buildTree(preorder[1: 1 + index], inorder[0: index])
        node.right = self.buildTree(preorder[1 + index:], inorder[index + 1: ])

        return node