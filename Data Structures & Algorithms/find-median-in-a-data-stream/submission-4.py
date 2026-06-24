class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)
        num = heapq.heappop(self.max_heap) * -1
        heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)
        
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # O(1), O(1)
    