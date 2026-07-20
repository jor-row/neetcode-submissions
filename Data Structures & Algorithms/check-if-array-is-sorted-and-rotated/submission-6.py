class Solution:
    def check(self, nums: List[int]) -> bool:
        #find breakpoints
        count = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                count += 1

        print(count)

        return True if count <= 1 else False
        