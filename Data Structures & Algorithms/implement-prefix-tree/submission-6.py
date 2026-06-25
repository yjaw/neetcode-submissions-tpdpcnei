class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['.'] = {}
        # O(N), O(N)
    def serach_helper(self, target: str) -> dict:
        cur = self.root
        for c in target:
            if c not in cur:
                return None
            cur = cur[c]
        return cur
        #O(N), O(1)
    def search(self, word: str) -> bool:
        last_char = self.serach_helper(word)
        if not last_char or '.' not in last_char:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        last_char = self.serach_helper(prefix)
        if not last_char:
            return False
        return True
        