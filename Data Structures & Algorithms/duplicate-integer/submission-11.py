class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set0 = set()
        for i in nums:
            if i in set0:
                return True
            else:
                set0.add(i)
        return False    

