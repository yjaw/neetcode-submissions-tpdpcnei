from heapq import heappop, heappush
class MedianFinder:
    ## 1. 永遠先推入 max_heap
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def switchNum(self, num: int, heap: list) -> int:
        if not heap: return num
        heappush(heap, num)
        return heappop(heap)

    def addNum(self, num: int) -> None:
        if self.max_heap and -num > self.max_heap[0]:
            num = -1 * self.switchNum(-num, self.max_heap)
        elif self.min_heap and num > self.min_heap[0]:
            num = self.switchNum(num, self.min_heap)

        if len(self.max_heap) == len(self.min_heap):
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        return None


    def findMedian(self) -> float:
        if not self.max_heap and not self.min_heap: return 0.0;
        if len(self.max_heap) - len(self.min_heap) == 1:
            return self.max_heap[0] * -1
        else:
            return ((self.max_heap[0] * -1 + self.min_heap[0]) / 2)
        