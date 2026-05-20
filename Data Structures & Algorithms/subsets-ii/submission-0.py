class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx: int, cur: list) -> None:
            res.append(cur[:])

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: 
                    continue
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()
        
        backtrack(0, [])
        return res
       