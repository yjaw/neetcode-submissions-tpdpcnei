class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 建圖：只收錄出現過的字母
        graph = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # ["abc", "ab"] 是無效輸入
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break  # 只取第一個不同字元

        # Topological sort (DFS)，偵測 cycle
        # 0 = 未訪問, 1 = 訪問中, 2 = 完成
        state = {c: 0 for c in graph}
        res = []

        def dfs(c: str) -> bool:
            if state[c] == 1: return False  # cycle
            if state[c] == 2: return True   # 已處理
            state[c] = 1
            for nei in graph[c]:
                if not dfs(nei):
                    return False
            state[c] = 2
            res.append(c)
            return True

        for c in graph:
            if not dfs(c):
                return ""

        return "".join(reversed(res))