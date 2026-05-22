class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        cost = [float('inf')] * (n + 1)
        cost[0] = 0
        cost[k] = 0

        visited = set()

        for _ in range(n):
            temp = cost[:]
            for u, v, t in times:
                if cost[u] + t < temp[v]:
                    temp[v] = cost[u] + t
            cost = temp

        res = max(cost)
        print(cost)
        return -1 if res == float('inf') else res
