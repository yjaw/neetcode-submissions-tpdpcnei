class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        max_idx = nums[0]
        cur_idx = 0

        while cur_idx < len(nums):
            if cur_idx == len(nums) - 1:
                return res
            res += 1
            n = max_idx
            while cur_idx < n:
                cur_idx += 1
                if cur_idx == len(nums) - 1:
                    break
                max_idx = max(max_idx, cur_idx + nums[cur_idx])
        return res