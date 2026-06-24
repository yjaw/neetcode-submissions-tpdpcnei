class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        left = -self.max_heap[0] if self.max_heap else float('-inf')
        right = self.min_heap[0] if self.min_heap else float('inf')
        if num < left:
            heapq.heappush(self.max_heap, -num)
            num = -heapq.heappop(self.max_heap)
        elif num > right:
            heapq.heappush(self.min_heap, num)
            num = heapq.heappop(self.min_heap)
            
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        print(self.max_heap, self.min_heap)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        