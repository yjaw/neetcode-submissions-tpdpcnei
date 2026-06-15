class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            n = len(st)
            cur = str(n) + '#' + st
            res.append(cur)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i: j])
            res.append(s[j + 1: j + 1 + n])
            i = j + 1 + n
        return res