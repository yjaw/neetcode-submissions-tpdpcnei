class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        nums = digits[::-1]

        for i in range(len(nums)):
            cur = nums[i]
            cur += carry
            carry = cur // 10
            cur %= 10
            nums[i] = cur
            if carry == 0:
                break
        
        if carry != 0:
            nums.append(carry)
        
        return nums[::-1]