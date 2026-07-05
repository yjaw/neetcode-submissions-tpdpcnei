class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('-inf')]

        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                i = 0
                while dp[i] < num:
                    i += 1
                dp[i] = num
            print(dp)
        return len(dp) - 1
