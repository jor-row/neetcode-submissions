class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # build a prefix and a postfix array
        if len(nums) == 0:
            return -1

        pre = [0 for i in range(len(nums))]
        post = [0 for i in range(len(nums))]

        pre[0] = nums[0]
        post[-1] = nums[-1]

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] + nums[i]
            post[len(nums) - i - 1] = post[len(nums) - (i + 1) + 1] + nums[len(nums) - i - 1]

        print(pre)
        print(post)

        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i
        return -1
