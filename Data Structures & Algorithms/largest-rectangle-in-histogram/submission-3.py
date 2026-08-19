class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            h = heights[i]
            start = i

            while stack and stack[-1][1] > h:
                pop_i, pop_h = stack.pop()
                res = max(res, (i - pop_i) * pop_h)
                start = pop_i
            stack.append((start, h))
            #print(res)
        
        while stack:
            pop_i, pop_h = stack.pop()
            res = max(res, (len(heights) - pop_i) * pop_h)
            #print(res)

        return res