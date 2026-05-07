class Node:

    def __init__(self):
        self.next: Node = None
        self.pre: Node = None
        self.val = 0
        self.key = 0

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = dict()
        self.count = 0
        self.cap = capacity

    def unlink(self, node: Node) -> None:
        node.next.pre, node.pre.next = node.pre, node.next

    def add(self, node: Node) -> None:
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.unlink(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.unlink(self.cache[key])
            self.add(self.cache[key])
        else:
            self.count += 1
            self.cache[key] = Node()
            self.cache[key].val = value
            self.cache[key].key = key
            self.add(self.cache[key])

        if self.count > self.cap:
            self.count -= 1
            del self.cache[self.tail.pre.key]
            self.unlink(self.tail.pre)
            

        
