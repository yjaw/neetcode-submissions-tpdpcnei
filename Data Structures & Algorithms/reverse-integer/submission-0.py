class Solution:
    def reverse(self, x: int) -> int:
        signal = '+'
        if x < 0:
            signal = '-'
            x = -x
        res = 0

        while x > 0:
            digi = x % 10
            res *= 10
            res += digi
            x //= 10
        
        res = res if signal == '+' else -res
        return res if (-2 ** 31 <= res <= 2 ** 31 - 1) else 0