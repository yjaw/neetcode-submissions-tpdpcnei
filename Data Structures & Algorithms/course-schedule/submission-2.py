class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = defaultdict(list)
        finish = 0
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            cmap[b].append(a)
            in_degree[a] += 1
        que = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                que.append(i)
        
        while que:
            cur = que.popleft()
            finish += 1
            for a in cmap[cur]:
                in_degree[a] -= 1
                if in_degree[a] == 0:
                    que.append(a)

        return finish == numCourses
        # O(V + E), O(V)