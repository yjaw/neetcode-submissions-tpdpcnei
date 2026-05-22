class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i1 = 0
        i2 = 0

        if len(s1) + len(s2) != len(s3):
            return False
        
        for c in s3:
            c1 = "" if i1 == len(s1) else s1[i1]
            c2 = "" if i2 == len(s2) else s2[i2]

            if c == c2:
                i2 += 1
            elif c == c1:
                i1 += 1
            else:
                return False
        
        return True
