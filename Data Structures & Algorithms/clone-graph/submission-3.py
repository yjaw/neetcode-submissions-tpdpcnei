"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        # BFS make a copy before add in a que
        que = deque()
        node_map = {}
        node_map[node] = Node(node.val)
        que.append(node)

        while que:
            cur = que.popleft()
            for next_node in cur.neighbors:
                if next_node not in node_map:
                    node_map[next_node] = Node(next_node.val)
                    que.append(next_node)

                node_map[cur].neighbors.append(node_map[next_node])
        return node_map[node]