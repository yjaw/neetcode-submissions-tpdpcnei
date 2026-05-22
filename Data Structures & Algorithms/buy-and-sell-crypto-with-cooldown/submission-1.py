class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold     = -prices[0]  # holding a stock
        ready    = 0           # can buy
        cooldown = 0           # just sold, in cooldown

        for price in prices[1:]:
            pre_hold, pre_ready, pre_cool = hold, ready, cooldown
            hold     = max(pre_hold, pre_ready - price)
            ready    = max(pre_ready, pre_cool)
            cooldown = pre_hold + price

        return max(ready, cooldown)