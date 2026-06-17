class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = [0] * 26

        lo, hi = 0, 0

        while hi < len(s):
            count[ord(s[hi]) - ord('A')] += 1
            hi += 1

            while sum(count) - max(count) > k:
                count[ord(s[lo]) - ord('A')] -= 1
                lo += 1

            res = max(res, hi - lo)
        
        return res
