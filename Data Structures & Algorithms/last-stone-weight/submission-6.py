class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            if stones[-1] > stones[-2]:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
            elif stones[-1] < stones[-2]:
                stones[-2] = stones[-2] - stones[-1]
                stones.pop(-1)
            else:
                stones.pop(-1)
                stones.pop(-1)

            stones.sort()

        if len(stones) == 0:
            return 0

        return stones[0]
        