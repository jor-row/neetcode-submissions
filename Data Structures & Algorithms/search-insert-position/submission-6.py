class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) //2
            n = nums[m]

            if n == target:
                return m
            elif n > target:
                r=m-1
            else:
                l=m+1
        return l