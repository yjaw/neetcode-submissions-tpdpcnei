class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [[1, -1] for _ in range(len(nums))]

        for i in range(len(nums)):
            cur_max = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] and mem[j][0] > cur_max:
                    cur_max = mem[j][0]
                    mem[i][0] = cur_max + 1
                    mem[i][1] = j
        
        start = 0
        n = 0
        for i in range(len(mem)):
            cur_n, pre_idx = mem[i]
            if cur_n >= n:
                n = cur_n
                start = i
       
        res = []
        idx = start
        while True:
            res.append(nums[idx])
            if mem[idx][1] == -1:
                break
            else:
                idx = mem[idx][1]
        
        #print(res[::-1])
        return n
