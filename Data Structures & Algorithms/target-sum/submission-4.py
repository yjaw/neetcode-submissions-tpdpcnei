class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        res = 0
        for i in range(1, len(nums)):
            li = dp.keys()
            level_dp = defaultdict(int)
            for j in list(li):
                level_dp[j - nums[i]] += dp[j]
                level_dp[j + nums[i]] += dp[j]
            dp = level_dp

        return dp[target]