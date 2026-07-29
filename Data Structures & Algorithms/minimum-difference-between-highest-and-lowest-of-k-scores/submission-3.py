class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 10000001
        print(nums)

        for i in range(len(nums) - k+1):
            print(nums[i:i+k])
            print(nums[i+k-1])
            print(nums[i])
            diff = nums[i+k-1] - nums[i]
            res = min(res, diff)

        return res
        