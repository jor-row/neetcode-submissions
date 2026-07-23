class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert = len(nums) - 1
        i = 0
        k = len(nums)

        while i < k:
            if nums[i] == val:
                nums[i], nums[insert] = nums[insert], nums[i]
                insert -= 1
                k -= 1
            else:
                i += 1
            print(nums)

        return k