class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            count = 1
            pre_max = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] and mem[j] > pre_max:
                    pre_max = mem[j]
            mem[i] = count + pre_max;

        #print(mem)
        return max(mem);