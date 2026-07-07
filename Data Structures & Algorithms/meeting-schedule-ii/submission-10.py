"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        pq = []
        res = 0
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            start, end = interval.start, interval.end
            while pq and pq[0] <= start:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
            res = max(res, len(pq))
        return res