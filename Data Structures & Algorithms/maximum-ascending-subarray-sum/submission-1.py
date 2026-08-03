class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        prev = 0

        for num in nums:
            if num > prev:
                curr += num
                print(curr)
                prev = num
            else:
                res = max(res, curr)
                curr = num
                prev = num

        return max(res, curr)
        