class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we split array into 2 half and always check the one is sorted
        # if t is not in the sorted one. we know t is locate at the other half
        # conversely, t locate at the sorted one. -> keep the b-search till find the t.

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid - 1
        
        return -1
