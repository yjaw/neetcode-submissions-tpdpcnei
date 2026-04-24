class PrefixTree:

    def __init__(self):
        self.trie = defaultdict(dict)


    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = defaultdict(dict)
            cur = cur[c]
        cur["."] = None
        #print(self.trie)
        

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        #print(cur)
        return True if "." in cur else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        
        return True
        