class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i in range(len(nums)):
            num = nums[i]

            while q and nums[q[-1]] <= num:
                q.pop()
            
            q.append(i)

            while q and q[0] <= i - k:
                q.popleft()
            
            if i >= k - 1:
                res.append(nums[q[0]])

        return res