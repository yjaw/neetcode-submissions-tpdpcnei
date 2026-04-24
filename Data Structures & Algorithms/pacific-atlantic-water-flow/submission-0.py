class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(heights)
        m = len(heights[0])
        mark = [[0] * m for _ in range(n)]
        res = []

        pac = 1
        atl = 2
        def move(i: int, j: int, sea: int) -> None:
            if mark[i][j] != sea and mark[i][j] != pac + atl:
                mark[i][j] += sea
                for ni, nj in direction:
                    ni += i
                    nj += j
                    if 0 <= ni < n and 0 <= nj < m and heights[i][j] <= heights[ni][nj]:
                        move(ni, nj, sea)
            return
        
        for i in range(n):
            move(i, 0, pac)
            move(i, m - 1, atl)
        for j in range(m):
            move(0, j, pac)
            move(n - 1, j, atl)

        for i in range(n):
            for j in range(m):
                if mark[i][j] == pac + atl:
                    res.append([i, j])
        return res