class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        in_pq = defaultdict(int)
        pq = []

        lo = 0
        hi = 0

        for _ in range(k):
            in_pq[nums[hi]] += 1
            heapq.heappush(pq, -nums[hi])
            hi += 1
        print("zz", pq)
        res = []
        while hi < len(nums):
            while pq and in_pq[-pq[0]] == 0:
                print(hi, "q", pq)
                heapq.heappop(pq)
            res.append(-pq[0])
            heapq.heappush(pq, -nums[hi])
            in_pq[nums[hi]] += 1
            hi += 1
            in_pq[nums[lo]] -= 1
            lo += 1
        while pq and in_pq[-pq[0]] == 0:
            heapq.heappop(pq)
        res.append(-pq[0])
        return res 