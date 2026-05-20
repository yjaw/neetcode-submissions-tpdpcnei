class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, abs(n))
        if n == 1:
            return x
        if n == 0:
            return 1
        
        nx = x * x

        if n % 2 == 0:
            return self.myPow(nx, n // 2)
        else:
            return self.myPow(nx, n // 2) * x