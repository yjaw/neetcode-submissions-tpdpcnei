class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_next = 0
        cur = 0

        while cur <= max_next:
            max_next = max(max_next, cur + nums[cur])
            if max_next >= len(nums) - 1:
                return True
            cur += 1
        
        return False
            