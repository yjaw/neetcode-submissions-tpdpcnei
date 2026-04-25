class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # start with a node
        visited = set()
        def dfs(cur: int) -> None:
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    dfs(neighbor)

        # restun how many time we start
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
        