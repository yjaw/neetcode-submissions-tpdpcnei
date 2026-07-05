class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lo = nums[0]
        hi = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            lo *= nums[i]
            hi *= nums[i]
            lo, hi = min(lo, hi, nums[i]), max(lo, hi, nums[i])
            res = max(res, hi)
        return res
        # O(N), O(1)