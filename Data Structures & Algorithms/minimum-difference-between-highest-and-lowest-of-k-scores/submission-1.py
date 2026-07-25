class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1000000000

        for i in range(len(nums) - k + 1):
            subarr = nums[i:i+k]
            print(subarr)
            res = min(res, abs(subarr[-1] - subarr[0]))
            # print(subarr[0])
            # print(subarr[-1])
            # print(subarr[-1] - subarr[0])
            # print(abs(subarr[-1] - nums[0]))

        return res
