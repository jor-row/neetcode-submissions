class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}

        for i, num in enumerate(nums):
            if num not in count:
                count[num] = [i]
            else:
                count[num].append(i)


        for c in count:
            if len(count[c]) > 1:
                array = count[c]
                
                for i in range(len(array) - 1):
                    for j in range(i+1, len(array)):
                        if abs(array[i] - array[j]) <= k:
                            return True

        return False