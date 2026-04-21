class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                if (s[i: i + len(word)] == word) and (i == 0 or dp[i - 1] == True):
                    dp[i + len(word) - 1] = True
        print(dp)
        return dp[-1]