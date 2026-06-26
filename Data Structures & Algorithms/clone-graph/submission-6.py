"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {node: Node(val = node.val)}
        que = deque([node])
        while que:
            cur = que.popleft()
            for next_node in cur.neighbors:
                if next_node not in cloneMap:
                    que.append(next_node)
                    cloneMap[next_node] = Node(val = next_node.val)
                cloneMap[cur].neighbors.append(cloneMap[next_node])    
                    
        return cloneMap[node]
        # O(N), O(N)
