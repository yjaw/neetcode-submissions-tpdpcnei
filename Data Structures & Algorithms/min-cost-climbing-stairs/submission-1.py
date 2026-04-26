class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start from -1, end of n, return min cost
        # move 1 or 2 step in one time
        pre2 = 0
        pre1 = 0

        for i in range(2, len(cost) + 1):
            cur = min(pre2 + cost[i - 2], pre1 + cost[i - 1])
            pre2, pre1 = pre1, cur

        return pre1