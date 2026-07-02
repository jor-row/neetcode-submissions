class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        count = 0

        if len(nums) == 1 and nums[0] == target:
            return 0
        
        while a < b:
            if nums[a] == target:
                return a
            elif nums[b] == target:
                return b

            indexToCheck = (b + a)

            if indexToCheck % 2 == 0:
                indexToCheck = indexToCheck // 2
            else:
                indexToCheck = indexToCheck // 2 + 1

            if nums[indexToCheck] == target:
                return indexToCheck

            if nums[indexToCheck] > target:
                if indexToCheck == b:
                    return -1
                b = indexToCheck
            else:
                a = indexToCheck
      
        return -1

        