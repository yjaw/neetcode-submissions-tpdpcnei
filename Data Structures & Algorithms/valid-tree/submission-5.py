class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree -> No cycle & one tree
        tmap = defaultdict(list)
        visited = set()

        for a, b in edges:
            tmap[a].append(b)
            tmap[b].append(a)

        que = deque([(0, -1)])
        while que:
            cur, pre = que.popleft()
            visited.add(cur)
            for next_node in tmap[cur]:
                if next_node == pre:
                    continue
                if next_node in visited:
                    return False
                que.append((next_node, cur))
        
        return len(visited) == n
        # O(V), O(V)