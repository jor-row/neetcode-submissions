class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        rowLen = 1

        while n > 0:
            if n >= rowLen:
                count +=1
                n -= rowLen
                rowLen += 1
            else:
                n = -1

        return count
            
        