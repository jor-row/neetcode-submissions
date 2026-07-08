class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = 0
        count = 0

        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            maxCount = max(count, maxCount)

        return maxCount