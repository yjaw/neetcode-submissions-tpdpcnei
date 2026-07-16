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
            j = s.find('#', i) # find next 'substring' after index i
            n = int(s[i: j])
            res.append(s[j + 1: j + 1 + n])
            i = j + 1 + n
        return res