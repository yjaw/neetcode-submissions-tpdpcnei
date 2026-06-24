# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        que = deque([root])
        while que:
            cur = que.popleft()
            if not cur:
                res.append('N')
            else:
                res.append(str(cur.val))
                que.append(cur.left)
                que.append(cur.right)
        res = "/".join(res)
        print(res)
        return res
        # T: O(N), S: O(N)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        level_order = data.split('/')
        if level_order[0] == 'N':
            return None
        print(level_order)
        que = deque(level_order)
        node_que = deque()
        root_val = que.popleft()
        root = TreeNode(val = int(root_val))
        node_que.append(root)
        while node_que:
            cur = node_que.popleft()
            left_val = que.popleft()
            right_val = que.popleft()
            if left_val != 'N':
                cur.left = TreeNode(val = int(left_val))
                node_que.append(cur.left)
            if right_val != 'N':
                cur.right = TreeNode(val = int(right_val))
                node_que.append(cur.right)

        return root
        # T: O(N), S: O(N)