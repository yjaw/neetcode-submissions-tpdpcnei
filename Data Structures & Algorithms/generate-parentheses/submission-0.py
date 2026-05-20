class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left: int, right: int, cur: list) -> None:
            if right == n:
                res.append("".join(cur))
                return
            
            if left < n:
                cur.append("(")
                helper(left + 1, right, cur)
                cur.pop()
            
            if left > right:
                cur.append(")")
                helper(left, right + 1, cur)
                cur.pop()
        
        helper(0, 0, [])
        return res