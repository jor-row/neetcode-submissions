class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)

        new_s = ""

        for i in range(count["1"] - 1):
            new_s += "1"

        for j in range(count["0"]):
            new_s += "0"

        return new_s + "1"
        