class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] # (temp, idx)
        res = []
        
        for i in range(len(temp) - 1, -1, -1):
            while stack and stack[-1][0] <= temp[i]:
                stack.pop()

            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)

            stack.append((temp[i], i))

        return res[::-1] 