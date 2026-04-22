class Solution:
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def dfs(self, board: List[List[str]], word: str, index: int, row: int, col: int) -> bool:
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:
            return False
        if board[row][col] != word[index]:
            return False
        if index == len(word) - 1 and board[row][col] == word[index]:
            return True
        
        mem = board[row][col]
        board[row][col] = "."
        for next_row, next_col in self.dir:
            next_row += row
            next_col += col
            if self.dfs(board, word, index + 1, next_row, next_col):
                return True
        board[row][col] = mem

        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0: return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, 0, i, j):
                    return True
        
        return False
                    