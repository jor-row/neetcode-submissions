class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lastIndexWithSmallerNum = -1

        for i, num in enumerate(nums):
            if target == num:
                return i
            elif num < target:
                lastIndexWithSmallerNum += 1


        return lastIndexWithSmallerNum + 1