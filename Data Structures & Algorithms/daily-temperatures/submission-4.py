class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] # idx
        res = []
        
        for i in range(len(temp) - 1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()

            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)

            stack.append(i)

        return res[::-1] 