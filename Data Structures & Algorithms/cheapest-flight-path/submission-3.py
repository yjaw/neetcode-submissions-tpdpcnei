class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for sc, dt, pz in flights:
            graph[sc].append((dt, pz))

        prices = defaultdict(int)
        pq = [(0, src, 0)] # price to i / i / ways to i

        while pq:
            pz, cur, way = heapq.heappop(pq)
            if cur == dst:
                return pz

            if way + 1 <= k + 1:
                for nex, money in graph[cur]:
                    heapq.heappush(pq, (pz + money, nex, way + 1))
        
        return -1