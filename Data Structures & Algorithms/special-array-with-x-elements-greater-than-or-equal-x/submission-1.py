class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0 for i in range(1001)]

        for num in nums:
            count[num] += 1

        i = len(count) - 2

        while i >= 0:
            count[i] += count[i+1]
            i-=1


        for i, x in enumerate(count):
            if i == x:
                return x


        return -1

        
        