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
        if not head:
            return head
        node_map = dict()
        node_map[head] = Node(head.val)
        node_map[None] = None
        cur = head
        while cur:
            if cur.next not in node_map:
                node_map[cur.next] = Node(cur.next.val)
            if cur.random not in node_map:
                node_map[cur.random] = Node(cur.random.val)
            node_map[cur].next = node_map[cur.next]
            node_map[cur].random = node_map[cur.random]
            cur = cur.next
        
        return node_map[head]
                