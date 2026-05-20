class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pal(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(idx: int, cur: list) -> None:
            if idx == len(s):
                res.append(cur[:])
            
            for i in range(idx, len(s)):
                sub = s[idx: i + 1]
                if is_pal(sub):
                    cur.append(sub)
                    backtrack(i + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res
        