class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2

        dp = set([0])

        for num in nums:
            level_dp = set()
            for reach in dp:
                level_dp.add(reach + num)
            dp = dp | level_dp
        
        return half in dp