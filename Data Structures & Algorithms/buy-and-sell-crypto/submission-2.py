class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]

        for i in range(1, len(prices)):
            res = max(res, prices[i] - cur)
            cur = min(cur, prices[i])
        
        return res