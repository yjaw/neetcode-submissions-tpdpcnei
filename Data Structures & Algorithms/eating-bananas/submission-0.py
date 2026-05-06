class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = 1
        while lo <= hi:
            mid = (lo + hi) // 2

            spend_h = 0
            for ban in piles:
                spend_h += (ban + mid - 1) // mid
            
            print(mid, spend_h)
            if spend_h <= h:
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
        
        return res