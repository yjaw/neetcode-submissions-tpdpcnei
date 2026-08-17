class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # 儲存 (index, height)

        for i, h in enumerate(heights):
            start = i
            # 當當前高度比堆疊頂端矮時，彈出並計算面積
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # 當前柱子可以向左延伸到被彈出柱子的位置
            
            stack.append((start, h))

        # 處理堆疊中殘留的柱子（它們都可以延伸到最右邊）
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area