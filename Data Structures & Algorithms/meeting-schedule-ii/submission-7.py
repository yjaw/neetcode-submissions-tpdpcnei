"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        room = [0] * 1000005
        for interval in intervals:
            lo, hi = interval.start, interval.end
            for i in range(lo, hi):
                room[i] += 1
                res = max(res, room[i])
        return res