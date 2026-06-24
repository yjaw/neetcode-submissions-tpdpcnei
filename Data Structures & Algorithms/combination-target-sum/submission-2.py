class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(cur_list: list, cur_sum: int, index: int) -> None:
            if cur_sum == target:
                res.append(list(cur_list))
                return
            if cur_sum > target or index >= len(nums):
                return
            
            cur_list.append(nums[index])
            helper(cur_list, cur_sum + nums[index], index)
            cur_list.pop()
            helper(cur_list, cur_sum, index + 1)

        helper([], 0, 0)
        return res

        # O(2^N), O(N)