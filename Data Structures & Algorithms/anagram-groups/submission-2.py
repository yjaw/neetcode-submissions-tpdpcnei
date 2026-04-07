class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for sub_str in strs:
            count = [0] * 26
            for c in sub_str:
                count[ord(c) - ord('a')] += 1
            mem[tuple(count)].append(sub_str)
        
        ans = []
        for _, sub_strs in mem.items():
            ans.append(sub_strs)
        return ans
