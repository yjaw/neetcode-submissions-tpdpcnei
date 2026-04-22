class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        que = deque()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    que.append((i, j))
                    res += 1
                    while que:
                        x, y = que.popleft()
                        grid[x][y] = '0'
                        
                        for nx, ny in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx += x
                            ny += y
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                                que.append((nx, ny))

        return res