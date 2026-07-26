class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        count = Counter(bin(n))
        print(count)
        return count["1"]