class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            k = (lo + hi) // 2
            time = 0
            for pile in piles:
                time += (pile - 1) // k + 1
            # print(k, time)
            if time <= h:
                hi = k
            else:
                lo = k + 1
        return hi