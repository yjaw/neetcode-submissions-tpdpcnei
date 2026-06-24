class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i: int, row: int, col: int) -> bool:
            if i == len(word):
                return True
            if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] != word[i]:
                return False
            
            temp = board[row][col]
            board[row][col] = '.'
            for nx, ny in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                next_row = nx + row
                next_col = ny + col
                if dfs(i + 1, next_row, next_col):
                    return True
            board[row][col] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        return False
