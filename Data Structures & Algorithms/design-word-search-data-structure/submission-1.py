class Node:
    def __init__(self):
        self.next_char = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next_char:
                cur.next_char[c] = Node()
            cur = cur.next_char[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def helper(cur: Node, index: int) -> bool:
            if cur.is_end and index == len(word):
                return True
            if index == len(word): return False
            c = word[index]
            
            if c in cur.next_char:
                return helper(cur.next_char[c], index + 1)
            if c == '.':
                for next_c in cur.next_char:
                    if helper(cur.next_char[next_c], index + 1): return True
            return False

        return helper(self.root, 0)
