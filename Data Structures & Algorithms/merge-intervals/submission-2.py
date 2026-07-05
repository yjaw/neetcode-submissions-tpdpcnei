class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur_start, cur_end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if cur_end < start:
                res.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            else:
                cur_end = max(cur_end, end)
        res.append([cur_start, cur_end])
        return res
        # O(N), O(N)