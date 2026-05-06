class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check1 = defaultdict(set)
        check2 = defaultdict(set)

        check5 = defaultdict(set)

        ["5","3",".",".","7",".",".",".","."]
        ["6",".",".","1","9","5",".",".","."]
        [".","9","8",".",".",".",".","6","."]
        ["8",".",".",".","6",".",".",".","3"]
        ["4",".",".","8",".","3",".",".","1"]
        ["7",".",".",".","2",".",".",".","6"]
        [".","6",".",".",".",".","2","8","."]
        [".",".",".","4","1","9",".",".","5"]
        [".",".",".",".","8",".",".","7","9"]
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                print((i // 3) * 3 + (j // 3))
                if c != '.':
                    if c not in check1[i] and c not in check2[j] and c not in check5[(i // 3) * 3 + (j // 3)]:
                        check1[i].add(c)
                        check2[j].add(c)
                        check5[(i // 3) * 3 + (j // 3)].add(c)
                    else:

                        return False
        
        return True