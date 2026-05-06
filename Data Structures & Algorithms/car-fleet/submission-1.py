class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(position[i], speed[i]) for i in range(len(speed))]
        car.sort(key = lambda x: x[0])
        res = 1
        cur = car[-1]
        for i in range(len(car) - 2, -1, -1):
            if (target - cur[0]) / cur[1] < (target - car[i][0]) / car[i][1]:
                cur = car[i]
                res += 1
        return res
            
