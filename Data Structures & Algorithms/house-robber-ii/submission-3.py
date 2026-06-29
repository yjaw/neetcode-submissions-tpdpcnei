class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob, not_rob = 0, 0
        res = 0
        for i in range(len(nums) - 1):
            rob, not_rob = not_rob + nums[i], max(rob, not_rob)
        res = max(res, rob, not_rob)

        rob, not_rob = 0, 0
        for i in range(1, len(nums)):
            rob, not_rob = not_rob + nums[i], max(rob, not_rob)
        res = max(res, rob, not_rob)

        return res