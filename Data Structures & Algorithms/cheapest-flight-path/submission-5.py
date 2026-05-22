class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]
            for sc, dt, pz in flights:
                if prices[sc] + pz < temp[dt]:
                    temp[dt] = prices[sc] + pz
            prices = temp

        return -1 if prices[dst] == float('inf') else prices[dst]  