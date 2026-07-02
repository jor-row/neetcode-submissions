class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)
        
        while a < b:
            mid = a + ((b - a) // 2)

            if nums[mid] >= target:
                b = mid
            elif nums[mid] < target:
                a = mid + 1
      
        return a if (a < len(nums) and nums[a] == target) else -1

        