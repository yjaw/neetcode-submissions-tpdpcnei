class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start: int, cur_sum: int, cur_list: List) -> None:
            nonlocal res
            if cur_sum == target:
                res.append(list(cur_list))
                return None
            elif cur_sum > target:
                return None

            for i in range(start, len(nums)):
                cur_list.append(nums[i])
                dfs(i, cur_sum + nums[i], cur_list)
                cur_list.pop()
        
        dfs(0, 0, [])
        return res
            
            