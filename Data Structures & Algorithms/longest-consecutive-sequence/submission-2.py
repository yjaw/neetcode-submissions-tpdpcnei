class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for num in nums:
            if num in hset:
                lo, hi = num, num
                while lo - 1 in hset:
                    lo -= 1
                    hset.remove(lo)
                while hi + 1 in hset:
                    hi += 1
                    hset.remove(hi)
                hset.remove(num)
                res = max(res, hi - lo + 1)
        return res

        # T: O(N) S: O(N)