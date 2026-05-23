class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        land = 2147483647
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    que.append((i, j))
        
        step = 0
        while que:
            k = len(que)
            step += 1
            for _ in range(k):
                i, j = que.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    di += i
                    dj += j
                    if 0 <= di < rows and 0 <= dj < cols and grid[di][dj] == land:
                        grid[di][dj] = step
                        que.append((di, dj))
        return
