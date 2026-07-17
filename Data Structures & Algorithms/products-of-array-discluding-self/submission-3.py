class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] = prefix[i] * post
            post *= nums[i]
        return prefix

        # T: O(N)
        # S: O(1) 在 LeetCode 的標準中，回傳所需的陣列通常不計入額外空間