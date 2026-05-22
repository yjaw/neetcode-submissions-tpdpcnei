class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = defaultdict(int)
        for i in range(len(s)):
            hmap[s[i]] = i
        
        res = []
        sub_start_at = 0
        sub_end_at = 0
        for i in range(len(s)):
            c = s[i]
            sub_end_at = max(sub_end_at, hmap[c])
            if i == sub_end_at:
                res.append(sub_end_at - sub_start_at + 1)
                sub_start_at = i + 1
        return res