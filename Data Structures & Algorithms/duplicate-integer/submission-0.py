class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if we use a set, checking that a value is in
        # a set in O(1)
        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False
