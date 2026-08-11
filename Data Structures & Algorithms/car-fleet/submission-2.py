class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()

        stack = []
        for i in range(n - 1, -1, -1):
            p, s = cars[i]
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)