class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        seen = set()

        while i < len(nums) - k:
            if nums[i] in seen:
                nums[i], nums[-1-k] = nums[-1-k], nums[i]
                k += 1
            else:
                seen.add(nums[i])
                i += 1

        j = 0

        while j < len(nums) - k - 1:
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
            else:
                j += 1
            # print(nums)
        return len(nums) - k

        