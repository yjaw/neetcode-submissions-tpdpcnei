class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        bucket = self.tmap[key]
        lo = 0
        hi = len(bucket) - 1
        res = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if bucket[mid][0] <= timestamp:
                res = bucket[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
