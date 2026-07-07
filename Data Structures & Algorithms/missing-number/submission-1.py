class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect = len(nums)
        count = 0
        for i in range(len(nums)):
            expect += i
            count += nums[i]
        return expect - count