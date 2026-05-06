class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            
            while stack and stack[-1][0] <= t:
                stack.pop()
            
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)
            
            stack.append((t, i))
        
        return res[::-1]