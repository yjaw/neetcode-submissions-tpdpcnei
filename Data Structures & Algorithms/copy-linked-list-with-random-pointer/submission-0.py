"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        node_map = dict()
        cur = head
        while cur:
            if cur not in node_map:
                node_map[cur] = Node(x = cur.val)
            if cur.next not in node_map:
                node_map[cur.next] = Node(x = cur.next.val) if cur.next else None
            if cur.random not in node_map:
                node_map[cur.random] = Node(x = cur.random.val) if cur.random else None
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next

        return node_map[head]            