class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
            
        f_lo = 0
        f_hi = 0

        def checkPalindrome(lo: int, hi: int) -> tuple:
            if s[lo] != s[hi]:
                return (lo, lo)            
            while lo > 0 and hi < len(s) - 1 and s[lo - 1] == s[hi + 1]:
                lo -= 1
                hi += 1
            return (lo, hi)

        for i in range(len(s) - 1):
            lo, hi = checkPalindrome(i, i)
            if (hi - lo) > (f_hi - f_lo):
                f_lo = lo
                f_hi = hi

            lo, hi = checkPalindrome(i, i + 1)
            if (hi - lo) > (f_hi - f_lo):
                f_lo = lo
                f_hi = hi
        
        return s[f_lo: f_hi + 1]
           


