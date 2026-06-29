class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        tmap = defaultdict(list)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            if len(a) <= len(b) and a == b[: len(a)]:
                continue
            seq = []
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    seq = [a[j], b[j]]
                    break
            if not seq:
                return ""
            tmap[seq[0]].append(seq[1]) 
            in_degree[seq[1]] += 1
        
        que = deque()
        for c, num in in_degree.items():
            if num == 0:
                que.append(c)
        
        res = []
        while que:
            cur = que.popleft()
            res.append(cur)
            for next_c in tmap[cur]:
                in_degree[next_c] -= 1
                if in_degree[next_c] == 0:
                    que.append(next_c)
        
        return "".join(res) if len(res) == len(in_degree) else ""
     