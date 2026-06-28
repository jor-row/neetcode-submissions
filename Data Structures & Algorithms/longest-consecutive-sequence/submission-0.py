class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l_s = 0
        nums_hash = Counter(nums)
        starters = []

        for num in nums_hash:
            if num - 1 not in nums_hash:
                starters.append(num)

        for starter in starters:
            count = 1
            seq_end = starter + 1

            while seq_end in nums_hash:
                count += 1
                seq_end += 1

            if count > l_s:
                l_s = count

        return l_s

