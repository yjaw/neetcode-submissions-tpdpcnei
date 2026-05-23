class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = 1
                    que = deque()
                    que.append((i, j))
                    grid[i][j] = 0
                    while que:
                        x, y = que.popleft()
                        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx, ny = dx + x, dy + y
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                que.append((nx, ny))
                                count += 1
                    res = max(res, count)
        return res