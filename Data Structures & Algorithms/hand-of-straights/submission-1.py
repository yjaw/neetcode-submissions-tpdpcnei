class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hmap = Counter(hand)

        for num in hand:
            if hmap[num] == 0:
                continue
            for i in range(groupSize):
                cur = num + i
                if cur not in hmap or hmap[cur] == 0:
                    return False
                hmap[cur] -= 1
        return True


