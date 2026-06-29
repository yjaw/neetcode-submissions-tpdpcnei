class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        visited = {"pac": set(), "atl": set()}

        def dfs(i: int, j: int, oce: int) -> None:
            if (i, j) in visited[oce]:
                return
            visited[oce].add((i, j))
            if oce == "atl" and (i, j) in visited["pac"]:
                res.append([i, j])

            for ni, nj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni += i
                nj += j
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]) and (ni, nj) not in visited[oce] and heights[i][j] <= heights[ni][nj]:
                    dfs(ni, nj, oce)
        
        for i in range(len(heights)):
            dfs(i, 0, "pac")
        for j in range(len(heights[0])):
            dfs(0, j, "pac")
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, "atl")
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, "atl")
        
        return res
        # O(N * M), O(N * M)
        