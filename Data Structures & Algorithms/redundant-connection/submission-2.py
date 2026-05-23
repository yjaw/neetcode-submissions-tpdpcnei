class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)] 

        def find(x: int) -> None:
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            par[px] = py
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        
        return []