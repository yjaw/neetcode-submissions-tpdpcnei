class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for ch in st:
                count[ord(ch) - ord('a')] += 1
            
            hmap[tuple(count)].append(st)
        res = []
        for k, v in hmap.items():
            res.append(v)
        return res