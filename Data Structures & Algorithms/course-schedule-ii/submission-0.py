class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b] = a need b

        graph = defaultdict(list)
        in_degrees = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degrees[a] += 1
        
        que = deque()
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                que.append(i)
        res = []
        while que:
            cur = que.popleft()
            res.append(cur)
            for course in graph[cur]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    que.append(course)
        
        return res if len(res) == numCourses else []
