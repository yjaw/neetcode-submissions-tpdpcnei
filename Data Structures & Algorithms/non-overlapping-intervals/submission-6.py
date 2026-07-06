class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        _, cur_e = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if cur_e <= s:
                cur_e = e
                
            else:
                cur_e = min(cur_e, e)
                res += 1

        return res
        # O(N log N), O(1)