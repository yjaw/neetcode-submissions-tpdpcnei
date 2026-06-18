class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = s + t
        count = Counter(t)
        flag = len(count)
        lo, hi = 0, 0

        while hi < len(s):
            if s[hi] in count:
                count[s[hi]] -= 1
                if count[s[hi]] == 0:
                    flag -= 1
            hi += 1
            while flag == 0:
                res = s[lo: hi] if (hi - lo) < len(res) else res
                
                if s[lo] in count:
                    count[s[lo]] += 1
                    if count[s[lo]] == 1:
                        flag += 1
                lo += 1
        
        return res if res != s + t else ""