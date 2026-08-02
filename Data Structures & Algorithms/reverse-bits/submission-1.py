class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        print(bin(n)[2:][::-1])

        binary = str(bin(n)[2:][::-1])
        n = len(binary)

        for i in range(n, 32):
            binary += "0"

        print(binary)
        return int(binary, 2)

