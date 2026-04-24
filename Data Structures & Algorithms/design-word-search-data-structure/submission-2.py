class TreeNode:
    def __init__(self):
        self.child: dict[str: TreeNode] = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TreeNode()
            cur = cur.child[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(cur: TreeNode, i: int) -> bool:
            if i == len(word):
                return cur.is_end
            
            if word[i] == '.':
                return any(dfs(cur.child[c], i + 1) for c in cur.child)
            if word[i] not in cur.child:
                return False
            return dfs(cur.child[word[i]], i + 1)
        return dfs(self.root, 0)
