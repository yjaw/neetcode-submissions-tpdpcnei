class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    res += 1
                    que = deque([(i, j)])
                    while que:
                        row, col = que.popleft()
                        for ni, nj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            ni += row
                            nj += col
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "1":
                                grid[ni][nj] = "0"
                                que.append((ni, nj))
        return res