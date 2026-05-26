class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]

        def dfs(x: int, y: int, prev: int) -> int:
            if x < 0 or y < 0 or x >= rows or y >= cols or matrix[x][y] <= prev:
                return 0
            if memo[x][y] != -1:
                return memo[x][y]

            step = 0
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                step = max(step, dfs(nx, ny, matrix[x][y]) + 1)
            memo[x][y] = step
            return step

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, float('-inf')))
        return res