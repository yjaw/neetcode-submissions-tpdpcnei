class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            spend_h = sum(math.ceil(ban / mid) for ban in piles)

            if spend_h <= h:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res