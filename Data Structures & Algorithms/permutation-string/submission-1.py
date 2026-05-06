class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        map1 = [0] * 123
        map2 = [0] * 123

        for c in s1:
            #print(ord(c))
            map1[ord(c)] += 1

        lo = 0
        hi = 0

        while hi < len(s1):
            map2[ord(s2[hi])] += 1
            hi += 1

        while hi < len(s2):
            if map1 == map2:
                return True
            map2[ord(s2[hi])] += 1
            map2[ord(s2[lo])] -= 1
            lo += 1
            hi += 1
        
        return True if map1 == map2 else False
