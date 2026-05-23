class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        res = 0
        que = deque()
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append((i, j))
        
        while que:
            k = len(que)
            for _ in range(k):
                x, y = que.popleft()
                for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx += x
                    ny += y
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        que.append((nx, ny))
            if que:
                res += 1
        return res if fresh == 0 else -1