class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        mem = [[-1] * cols for _ in range(rows)]
        res = 0
        def dfs(x: int, y: int, pre: int) -> int:
            nonlocal res
            if x < 0 or y < 0 or x >= rows or y >= cols or matrix[x][y] <= pre:
                return 0
            if mem[x][y] != -1:
                return mem[x][y]

            step = 0
            for nx, ny in [(1, 0), (0, 1), (-1, 0),(0, -1)]:
                nx += x
                ny += y
                step = max(step, dfs(nx, ny, matrix[x][y]) + 1)
            mem[x][y] = step
            res = max(res, step)

            print(x, y, step)
            return step

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, float('-inf'))
        return res
        