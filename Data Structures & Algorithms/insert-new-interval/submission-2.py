class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        for cur_start, cur_end in intervals:
            if cur_end < start:
                res.append([cur_start, cur_end])
                print(1)
            elif cur_start <= start <= cur_end or cur_start <= end <= cur_end:
                start = min(cur_start, start)
                end = max(cur_end , end)
                print(2)
            elif cur_start > end:
                res.append([start, end])
                start, end = cur_start, cur_end
                print(3)
        res.append([start, end])
        return res