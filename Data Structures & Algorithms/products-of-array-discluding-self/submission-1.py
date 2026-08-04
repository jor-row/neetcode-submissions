class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [num for num in nums]
        post = [num for num in nums]

        for i in range(1, len(pre)):
            pre[i] *= pre[i-1]

        for j in range(1, len(post)):
            post[-1-j] *= post[-1-j+1]

        print(pre)
        print(post)

        merge = []

        for i in range(len(nums)):
            if i == 0:
                merge.append(post[1])
            elif i < len(nums) - 1:
                print(post[i+1])
                print(pre[i-1])
                merge.append(post[i+1] * pre[i-1])
            else:
                merge.append(pre[i - 1])


        print(merge)
        return merge

        