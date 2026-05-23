class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [a, b] means a requires b
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        res = []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for course in graph[cur]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return res if len(res) == numCourses else []