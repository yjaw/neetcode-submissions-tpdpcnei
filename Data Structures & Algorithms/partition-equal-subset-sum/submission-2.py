class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2

        def backtrack(cur_sum: int, idx: int) -> bool:
            if cur_sum == half:
                return True
            if cur_sum > half:
                return False
            if idx == len(nums):
                return False
            
            return backtrack(cur_sum + nums[idx], idx + 1) or backtrack(cur_sum, idx + 1)

        return backtrack(0, 0) 