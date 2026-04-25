class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build a graph
        graph = defaultdict(list)
        for node_a, node_b in edges:
            if node_a == node_b: return False
            graph[node_a].append(node_b)
            graph[node_b].append(node_a) 
        # try to find circle. can not go back
        visited = set()
        print(graph)
        def dfs(pre: int, cur: int) -> bool:
            visited.add(cur)
            for nex in graph[cur]:
                if nex != pre:
                    if nex in visited:
                        return False
                    if not dfs(cur, nex):
                        return False
            return True
        res = dfs(-1, 0)
        return res if len(visited) == n else False