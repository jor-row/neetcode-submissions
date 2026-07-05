class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True

        for i in range(len(nums)):
            new_array = nums[i:] + nums[:i]
            if new_array == sorted(new_array):
                return True
        return False