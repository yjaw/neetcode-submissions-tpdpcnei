class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            n = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:n] == w2[:n]:
                return ""
            
            for j in range(n):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
            
        que = deque([c for c, v in in_degree.items() if v == 0])
        
        res = []
        print(graph)
        while que:
            c = que.popleft()
            res.append(c)
            for nc in graph[c]:
                in_degree[nc] -= 1
                if in_degree[nc] == 0:
                    que.append(nc)
        
        return "".join(res) if len(res) == len(in_degree) else ""
