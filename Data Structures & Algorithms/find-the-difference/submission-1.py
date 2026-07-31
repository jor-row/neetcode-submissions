class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        counts = Counter(s)

        for char in count:
            if count[char] > counts[char]:
                return char
        