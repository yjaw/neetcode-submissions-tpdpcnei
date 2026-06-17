class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lo = 0
        hi = 0
        hset = set()
        while hi < len(s):
            while s[hi] in hset:
                hset.remove(s[lo])
                lo += 1
            hset.add(s[hi])
            hi += 1
            res = max(res, hi - lo)
        
        return res