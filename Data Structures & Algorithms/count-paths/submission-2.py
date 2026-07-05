class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for _ in range(1, n):
            for i in range(m):
                dp[i] = dp[i] if i == 0 else dp[i] + dp[i - 1]
        return dp[m - 1]
        # O(M * N), O(M)