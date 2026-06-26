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
        # O(V + E), O(V)
        # 在面試或更嚴謹的場合中，對於圖（Graph）的題目，我們通常會用 $V$（Vertex，頂點數）和 $E$（Edge，邊數）來表示
        

