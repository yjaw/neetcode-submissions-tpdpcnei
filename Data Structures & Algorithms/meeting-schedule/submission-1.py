"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        cur_end = -1
        for interval in intervals:
            start, end = interval.start, interval.end
            if start < cur_end:
                return False
            cur_end = end
        return True