class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        pq = [(0, 0)]  # (cost, node_index)
        res = 0

        while len(visited) < n:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            res += cost

            for i in range(n):
                if i not in visited:
                    dist = abs(points[i][0] - points[node][0]) + \
                           abs(points[i][1] - points[node][1])
                    heapq.heappush(pq, (dist, i))

        return res