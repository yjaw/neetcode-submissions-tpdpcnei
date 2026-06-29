class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        tmap = defaultdict(list)
        in_degree = {c: 0 for word in words for c in word}
        
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
                            
            # 開始比對相異字元
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    tmap[a[j]].append(b[j])
                    in_degree[b[j]] += 1
                    break  # 找到了第一個不同字元，成功建圖，跳出內層 for
            else:
                # 【重點在這裡！】
                # 如果內層 for 迴圈「正常走完」而沒有觸發 break
                # 代表前面公共長度的字元完全一模一樣（例如 "abc" 和 "ab"）
                # 此時如果前字比較長，就是不合法的字典順序，直接返回空字串
                if len(a) > len(b):
                    return ""
        
        # 後續的 BFS 拓撲排序邏輯完全不變
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