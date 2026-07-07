class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = b
        mask =    0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while carry:
            a, carry = a ^ carry, (a & carry) << 1
            carry &= mask
            a &= mask
        return a if a <= max_int else ~(a ^ mask)