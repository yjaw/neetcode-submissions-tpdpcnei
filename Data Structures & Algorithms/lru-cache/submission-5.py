class Node:
    def __init__(self, val: int, key: int, pre: Node, next: Node):
        self.val = val
        self.key = key
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.tail = Node(val = 0, key = 0, pre = None, next = None)
        self.head = Node(val = 0, key = 0, pre = None, next = None)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cmap = dict()

    def get(self, key: int) -> int:
        if key not in self.cmap:
            return -1
        else:
            val = self.cmap[key].val
            self.delete(self.cmap[key])
            self.add(key, val)
            return val

    def put(self, key: int, value: int) -> None:
        if key in self.cmap:
            self.delete(self.cmap[key])
        if len(self.cmap) >= self.size:
            self.delete(self.head.next)
        self.add(key, value)
    
    
    def delete(self, node: Node) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.cmap[node.key]

    def add(self, key: int, value: int) -> None:
        node = Node(val = value, key = key, pre = None, next = None)
        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        self.cmap[key] = node

    
