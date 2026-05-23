class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(x: int, y: int) -> None:
            if board[x][y] != 'O':
                return
            board[x][y] = '.'
            for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx += x
                ny += y
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    dfs(nx, ny)
            
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1) # why I can't use -1 as idx here -> it mass up idx in dfs
        for j in range(len(board[0])):  
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
        return