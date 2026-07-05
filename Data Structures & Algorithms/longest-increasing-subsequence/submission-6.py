import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('-inf')]

        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                i = bisect.bisect_left(dp, num)
                dp[i] = num
            print(dp)
        return len(dp) - 1
        # O(N ^ 2), O(N)