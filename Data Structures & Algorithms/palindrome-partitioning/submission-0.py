class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(idx: int, cur: list) -> None:
            if idx == len(s):
                res.append(cur[:])
                return
            
            for i in range(idx, len(s)):
                sub = s[idx:i+1]
                if is_palindrome(sub):
                    cur.append(sub)
                    backtrack(i + 1, cur)
                    cur.pop()
        
        backtrack(0, [])
        return res
        