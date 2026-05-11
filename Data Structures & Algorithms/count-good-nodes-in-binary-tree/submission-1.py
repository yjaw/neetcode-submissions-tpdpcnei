class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            count = int(node.val >= max_val)
            max_val = max(max_val, node.val)
            return count + check(node.left, max_val) + check(node.right, max_val)

        return check(root, root.val)
            
