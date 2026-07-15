class Solution:
    def countBits(self, n: int) -> List[int]:
        bins = []

        for i in range(n+1):
            bins.append(f"{i:b}")

        for i, b in enumerate(bins):
            b_count = Counter(b)
            bins[i] = b_count["1"]

        return bins


        