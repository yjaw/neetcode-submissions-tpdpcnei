class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        path = []
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(pre:int, cur: int, cur_path: list, visited: set) -> bool:
            nonlocal path
            if cur in visited:
                cur_path.append(cur)
                i = 0
                print(cur_path)
                while cur_path[i] != cur:
                    i += 1
                path = cur_path[i:]
                print(path)
                return True
            
            visited.add(cur)
            cur_path.append(cur)
            for nex in graph[cur]:
                if nex != pre:
                    if dfs(cur, nex, cur_path, visited):
                        return True
            visited.remove(cur)
            cur_path.pop()
            return False
            
        dfs(0, 1, [], set())
        print(path)
        for i in range(len(edges) - 1, -1, -1):
            a, b = edges[i]
            if a in path and b in path:
                return edges[i]
        return []
