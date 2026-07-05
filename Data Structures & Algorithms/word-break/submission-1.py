class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start = deque([0])
        visited = set([0])

        while start:
            i = start.popleft()
            for word in wordDict:
                j = i + len(word)
                if j <= len(s) and s[i: j] == word:
                    if j == len(s):
                        return True
                    if j not in visited:
                        visited.add(j)
                        start.append(j)
        
        return False


