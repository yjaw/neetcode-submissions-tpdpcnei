class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next: 'Node' = None
        self.prev: 'Node' = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        self.cap = capacity

    def unlink(self, node: Node) -> None:
        node.next.prev, node.prev.next = node.prev, node.next

    def add(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.unlink(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.unlink(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add(node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.unlink(lru)
            del self.cache[lru.key]