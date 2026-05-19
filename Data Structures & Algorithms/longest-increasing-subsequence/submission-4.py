class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n  # track previous index in LIS

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # find the index where LIS ends
        end = max(range(n), key=lambda i: dp[i])

        # reconstruct path by walking prev backwards
        path = []
        idx = end
        while idx != -1:
            path.append(nums[idx])
            idx = prev[idx]

        print(path[::-1])
        return dp[end]