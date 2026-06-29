class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 1

        def check(lo: int, hi: int) -> int:
            count = 0
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
            return count
        
        for i in range(len(s) - 1):
            res += check(i, i)
            res += check(i, i + 1)
        
        return res
