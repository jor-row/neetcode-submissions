class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) ==  0:
            return False
        
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False

        count = 0
        i = 0

        while i < len(flowerbed) - 1:

            if i == 0:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    count += 1
                    i += 2
                else:
                    i += 1
            elif i < len(flowerbed) - 2:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                    count += 1
                    i += 2
                else:
                    i += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    count += 1
                i += 1

        print(count)

        return n <= count