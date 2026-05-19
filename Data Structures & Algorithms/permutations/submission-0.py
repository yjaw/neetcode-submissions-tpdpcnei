class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(used: set, cur: list) -> None:
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for num in nums:
                if num not in used:
                    cur.append(num)
                    used.add(num)
                    dfs(used, cur)
                    cur.pop()
                    used.remove(num)
            return 
        
        dfs(set(), [])
        return res