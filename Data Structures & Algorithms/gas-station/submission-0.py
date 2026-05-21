class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = [gas[i] - cost[i] for i in range(n)]
        
        
        start = 0
        while start < n:
            cur_gas = 0
            for i in range(n):
                cur_gas += remain[(start + i) % n]
                if cur_gas < 0:
                    start = start + i + 1
                    break
                if i == n - 1:
                    return start
        
        return - 1