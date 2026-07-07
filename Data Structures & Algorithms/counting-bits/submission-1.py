class Solution:
    def countBits(self, n: int) -> List[int]:
        if n <= 0:
            return [0]

        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                res[i] = res[i // 2]
            else:
                res[i] = res[i - 1] + 1
        return res