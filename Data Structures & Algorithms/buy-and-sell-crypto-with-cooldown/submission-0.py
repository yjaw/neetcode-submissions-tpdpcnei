class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0] 
        ready = 0
        cooldown = 0

        for i in range(1, len(prices)):
            price = prices[i]
            pre_hold = hold # hold a stock and can sell
            pre_ready = ready # able to buy stock
            pre_cool = cooldown # not able to buy stock

            # status: ready -> hold -> cooldown

            hold = max(pre_hold, pre_ready - price)
            ready = max(pre_ready, pre_cool)
            cooldown = pre_hold + price
        
        return max(hold, ready, cooldown)