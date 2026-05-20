class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        phone = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]}
        res = []
        def backtrack(idx: int, cur: list) -> None:
            if idx == len(digits):
                res.append("".join(cur))
                return
            
            for c in phone[digits[idx]]:
                cur.append(c)
                backtrack(idx + 1, cur)
                cur.pop()
            
        backtrack(0, [])
        return res