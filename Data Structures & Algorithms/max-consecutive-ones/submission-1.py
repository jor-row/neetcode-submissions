class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
                if curr > maxC:
                    maxC = curr
            else:
                curr = 0

        return maxC
        