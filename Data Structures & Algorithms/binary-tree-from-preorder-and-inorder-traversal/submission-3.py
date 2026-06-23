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
        # T: O(N ^ 2) S: O(H)
        # 面試官看到你的基本解之後，100% 會問：「能不能不要每次都用 .index() 找位置？
        # 能不能不要複製陣列？」
        # 優化的思路非常漂亮：
        # 用雜湊表（HashMap）消滅 .index()： 既然 inorder 裡的數值都是唯一的，
        # 我們可以先用一個 Dictionary 把「數值 $\rightarrow$ 索引位置」存起來，這樣以後查詢位置只要 $O(1)$！
        # 用雙指針（Pointers）消滅陣列切片： 我們不切片，改傳入邊界索引（例如 in_start, in_end），
        # 直接在原陣列上做範圍操作。