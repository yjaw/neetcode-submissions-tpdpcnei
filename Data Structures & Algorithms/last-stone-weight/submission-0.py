class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-w for w in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            rock_a = heapq.heappop(max_heap)
            rock_b = heapq.heappop(max_heap)

            remain = rock_a - rock_b
            if remain != 0:
                heapq.heappush(max_heap, remain)
        
        return 0 if len(max_heap) == 0 else -max_heap[0]
