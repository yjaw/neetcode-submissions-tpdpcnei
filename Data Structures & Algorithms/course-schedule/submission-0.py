class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 base

        count = {i: 0 for i in range(numCourses)}
        pre_course = defaultdict(list)

        for pre in prerequisites:
            count[pre[1]] += 1
            pre_course[pre[0]].append(pre[1])

        que = deque()
        for k, v in count.items():
            if v == 0:
                que.append(k)
        res = 0
        while que:
            take_course = que.popleft()
            res += 1
            for release in pre_course[take_course]:
                count[release] -= 1;
                if count[release] == 0:
                    que.append(release)
        
        return res == numCourses