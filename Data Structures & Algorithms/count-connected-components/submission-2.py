class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        gmap = defaultdict(list)
        res = 0

        for a, b in edges:
            gmap[a].append(b)
            gmap[b].append(a)
        
        visited = set()

        for i in range(n):
            if i not in visited:
                res += 1
                que = deque([i])
                while que:
                    cur = que.popleft()
                    visited.add(cur)
                    for next_node in gmap[cur]:
                        if next_node not in visited:
                            que.append(next_node)

        return res
        # O(N), O(N)