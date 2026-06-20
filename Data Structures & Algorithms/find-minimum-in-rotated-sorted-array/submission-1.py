class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case1: not rotated -> just return the first num.
        # case2: rotated -> split into half, min num locate at the half one that are sorted.
        # example1:  4, 5, [6], (1, 2, 3)
        # example2:  (4, 5, 6, [1]), 2, 3  

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            # case1
            if nums[lo] <= nums[hi]:
                return nums[lo]
            # case2
            if nums[lo] <= nums[mid]:
                lo = mid + 1
            elif nums[lo] > nums[mid]:
                hi = mid
        
        return -1