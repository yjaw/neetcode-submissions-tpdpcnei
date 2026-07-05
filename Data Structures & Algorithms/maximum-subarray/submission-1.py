class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = lo = hi = nums[0]
        
        for i in range(1, len(nums)):
            lo += nums[i]
            hi += nums[i]
            lo, hi = min(lo, hi, nums[i]), max(lo, hi, nums[i])
            res = max(res, hi)
        return res