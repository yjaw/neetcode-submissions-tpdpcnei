class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        used = set()
        while n > 1:
            if n in used:
                return False
            used.add(n)
            temp = 0
            while n > 0:
                digi = n % 10
                temp += digi ** 2
                n //= 10
            n = temp
            if n == 1:
                return True
        
        return False