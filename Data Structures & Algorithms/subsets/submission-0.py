class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def rec(cur: list, idx: int) -> None:
            if idx == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[idx])
            rec(cur, idx + 1)
            cur.pop()
            rec(cur, idx + 1)
            return
        
        rec([], 0)
        return res