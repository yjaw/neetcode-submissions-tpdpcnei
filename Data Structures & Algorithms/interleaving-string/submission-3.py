class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(1, m + 1):
            dp[0][j] = s1[j - 1] == s3[j - 1] and dp[0][j - 1]
        for i in range(1, n + 1):
            dp[i][0] = s2[i - 1] == s3[i - 1] and dp[i - 1][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                k = i + j - 1
                dp[i][j] = (s1[j - 1] == s3[k] and dp[i][j - 1]) or (s2[i - 1] == s3[k] and dp[i - 1][j])


        return dp[n][m]
