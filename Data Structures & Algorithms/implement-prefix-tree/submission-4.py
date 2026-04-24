class Node:
    def __init__(self):
        self.nextNode: dict[str: Node] = {}
        self.isEnd: bool = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.nextNode:
                cur.nextNode[c] = Node()
            cur = cur.nextNode[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.nextNode:
                return False
            cur = cur.nextNode[c]

        return cur.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.nextNode:
                return False
            cur = cur.nextNode[c]
            
        return True
        