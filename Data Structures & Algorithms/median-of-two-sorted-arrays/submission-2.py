class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lo = 0
        hi = len(nums1)
        total = (len(nums1) + len(nums2))
        half = (total + 1) // 2
        
        while lo <= hi:
            m = (lo + hi + 1) // 2
            n = half - m
            
            m1 = nums1[m - 1] if m - 1 >= 0 else float('-inf')
            m2 = nums1[m] if m < len(nums1) else float('inf')
            n1 = nums2[n - 1] if n - 1 >= 0 else float('-inf')
            n2 = nums2[n] if n < len(nums2) else float('inf')

            if m2 < n1:
                lo = m + 1
            elif n2 < m1:
                hi = m - 1
            elif m2 >= n1 and n2 >= m1:
                if total % 2 == 1:
                    return max(m1, n1)
                else:
                    return (max(m1, n1) + min(m2, n2)) / 2

        return 0.0

