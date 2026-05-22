class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                cur[0] = max(cur[0], triplet[0])
                cur[1] = max(cur[1], triplet[1])
                cur[2] = max(cur[2], triplet[2])
        
        return cur == target