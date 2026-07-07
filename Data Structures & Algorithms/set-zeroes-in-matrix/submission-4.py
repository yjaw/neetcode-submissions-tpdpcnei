class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row_zero = False
        col_zero = False
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if matrix[i][0] == 0:
                row_zero = True
                break
        for j in range(cols):
            if matrix[0][j] == 0:
                col_zero = True
                break
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0
        
        if row_zero:
            for i in range(rows):
                matrix[i][0] = 0

        if col_zero:
            for j in range(cols):
                matrix[0][j] = 0
        # O(N), O(1)