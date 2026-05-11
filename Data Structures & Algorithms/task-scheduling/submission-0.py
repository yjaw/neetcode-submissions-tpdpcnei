class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)
        res = 0
        cd = deque()
        
        while cd or max_heap:
            if len(cd) > 0 and res - cd[0][1] > n:
                cur = cd.popleft()[0]
                heapq.heappush(max_heap, cur)
            
            if len(max_heap) > 0:
                cur = -heapq.heappop(max_heap) - 1
                if cur > 0:
                    cd.append((-cur, res))

            res += 1
        return res