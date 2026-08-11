class Solution:
    def tribonacci(self, n: int) -> int:
        tribb = [0, 1, 1]

        if n < 3:
            return tribb[n]

        for i in range(3, n+1):
            new = tribb[i-1] + tribb[i-2] + tribb[i-3]
            tribb.append(new)

        print(tribb)

        return tribb[-1]
        