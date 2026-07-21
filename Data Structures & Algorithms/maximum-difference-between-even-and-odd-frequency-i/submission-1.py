class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd = []
        even = []

        for c in count:
            if count[c] % 2 == 0:
                even.append(count[c])
            else:
                odd.append(count[c])

        even.sort()
        odd.sort()

        return odd[-1] - even[0]