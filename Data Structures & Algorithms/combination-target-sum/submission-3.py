class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(cur_list: list, cur_sum: int, index: int) -> None:
            if cur_sum == target:
                res.append(list(cur_list))
                return
            if cur_sum > target or index >= len(nums):
                return
            
            for i in range(index, len(nums)):
                cur_list.append(nums[i])
                helper(cur_list, cur_sum + nums[i], i)
                cur_list.pop()
            return

        helper([], 0, 0)
        return res

        # O(2^N), O(N)