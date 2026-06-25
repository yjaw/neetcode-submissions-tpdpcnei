class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # build trie
        root = {}
        for word in words:
            cur = root
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["end"] = True
        
        res = []

        def dfs(cur: dict, i: int, j: int, sb: list) -> None:
            if "end" in cur and cur["end"]:
                res.append("".join(sb))
                cur["end"] = False
                            
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] == '.' or board[i][j] not in cur:
                return
            
            cur_char = board[i][j]
            sb.append(cur_char)
            board[i][j] = '.'
            for ni, nj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni += i
                nj += j
                dfs(cur[cur_char], ni, nj, sb)
            board[i][j] = cur_char
            sb.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j, [])
        
        return res