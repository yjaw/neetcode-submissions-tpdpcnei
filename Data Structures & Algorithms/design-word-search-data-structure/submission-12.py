class WordDictionary:

    def __init__(self):
        self.root = {}


    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["isEnd"] = {} 

    def search(self, word: str) -> bool:
        # r: {a}
        # a: {b}
        # b: {'end'}
        def dfs(cur: dict, i: list) -> bool:
            if i == len(word) and "isEnd" in cur:
                return True
            if i >= len(word):
                return False
            c = word[i]
            if c == '.':
                for k, v in cur.items():
                    if dfs(v, i + 1):
                        return True
                return False
            else:
                if c not in cur:
                    return False
                return dfs(cur[c], i + 1)

        return dfs(self.root, 0)