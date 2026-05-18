class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def backtrack(cur: list, idx: int, cur_sum: int) -> None:
            if cur_sum == target:
                res.append(cur[:])
                return
            if cur_sum > target:
                return
            for i in range(idx, len(candidates), 1):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, cur_sum + candidates[i])
                cur.pop()
            return
        
        backtrack([], 0, 0)
        return res
            