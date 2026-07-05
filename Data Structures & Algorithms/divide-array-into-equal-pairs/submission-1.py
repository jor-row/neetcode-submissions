class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        for count in counts:
            if counts[count] % 2 != 0:
                return False


        return True
        