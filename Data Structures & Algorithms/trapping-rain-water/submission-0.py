class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        r_wall = [0] * n
        l_wall = [0] * n

        for i in range(1, n):
            r_wall[i] = max(r_wall[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            l_wall[i] = max(l_wall[i + 1], height[i + 1])

        res = 0
        for i in range(n):
            res += max(min(r_wall[i], l_wall[i]), height[i]) - height[i]

        return res 