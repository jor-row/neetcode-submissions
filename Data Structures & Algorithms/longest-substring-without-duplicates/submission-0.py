class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r, maxL = 0, 1, 0

        letters = {s[0]: 0}

        while r < len(s):
            if s[r] in letters:
                prevL = l
                l = letters[s[r]] + 1

                for k in range(prevL, l):
                    letters.pop(s[k])
            else:
                maxL = max(maxL, r - l + 1)
                letters[s[r]] = r
                r += 1

        return maxL
        