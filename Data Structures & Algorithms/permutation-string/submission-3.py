class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        map1 = [0] * 26
        map2 = [0] * 26

        for c in s1:
            map1[ord(c) - ord('a')] += 1

        for hi in range(len(s2)):
            map2[ord(s2[hi]) - ord('a')] += 1
            if hi >= len(s1):
                map2[ord(s2[hi - len(s1)]) - ord('a')] -= 1
            if hi >= len(s1) - 1 and map1 == map2:
                return True

        return False