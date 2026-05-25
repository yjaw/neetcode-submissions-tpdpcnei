"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sort_by = [(interval.start, interval.end) for interval in intervals]
        sort_by.sort()
        heap = []
        res = 0
        print(sort_by)
        for start, end in sort_by:
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            res = max(res, len(heap))
        return res