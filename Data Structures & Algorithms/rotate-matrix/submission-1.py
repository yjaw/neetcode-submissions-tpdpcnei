class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols // 2):
                matrix[i][j], matrix[i][cols - 1 - j] = matrix[i][cols - 1 - j], matrix[i][j]

        for i in range(rows):
            for j in range(cols - i):
                matrix[i][j], matrix[rows - 1 - j][cols - 1 - i] = matrix[rows - 1 - j][cols - 1 - i], matrix[i][j]
        
