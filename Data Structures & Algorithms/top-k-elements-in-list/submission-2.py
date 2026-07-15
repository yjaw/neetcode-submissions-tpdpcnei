class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        for key, v in count.items():
            heapq.heappush(min_heap, (v, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [key for v, key in min_heap]