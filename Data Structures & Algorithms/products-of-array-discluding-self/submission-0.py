class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets construct the prefix array first

        i = 0
        pre = []

        while i < len(nums):
            if i == 0:
                pre.append(1)
            else:
                pre.append(pre[i-1] * nums[i-1])
            i += 1

        # lets construct the suffix array second

        j = len(nums) - 1
        suff = [0 for i in nums]

        while j >= 0:
            if j == len(nums) - 1:
                suff[j] = 1
            else:
                suff[j] = nums[j+1] * suff[j+1]

            j -= 1

        ans = []

        for k in range(len(nums)):
            ans.append(pre[k]*suff[k])

        return ans