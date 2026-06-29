class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        not_rob = 0

        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        
        return max(rob, not_rob)
            