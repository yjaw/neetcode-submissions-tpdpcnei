class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        offset = 31
        while n > 0:
            if n & 1 == 1:
                res += (1 << offset)
            offset -= 1
            n >>= 1
        return res
        # O(1), O(1)