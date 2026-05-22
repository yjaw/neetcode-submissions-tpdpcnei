class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        visited = set()

        pq = []
        for i in range(1, len(points)):
            dis = abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1])
            heapq.heappush(pq, (dis, i, 0))
        

        res = 0
        while len(visited) < len(points):
            dis, n1, n2 = heapq.heappop(pq)
            if n1 not in visited or n2 not in visited:
                res += dis
            if n1 not in visited:
                for i in range(len(points)):
                    if i != n1 and i not in visited:
                        dis = abs(points[i][0] - points[n1][0]) + abs(points[i][1] - points[n1][1])
                        heapq.heappush(pq, (dis, i, 0))
            if n2 not in visited:
                for i in range(len(points)):
                    if i != n2 and i not in visited:
                        dis = abs(points[i][0] - points[n2][0]) + abs(points[i][1] - points[n2][1])
                        heapq.heappush(pq, (dis, i, 0))
            visited.add(n1)
            visited.add(n2)

        return res
