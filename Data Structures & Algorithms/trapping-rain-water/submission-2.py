class Solution:
    def trap(self, height: List[int]) -> int:

        # i think the pointers need to start at the beginning for this
        # both have to be > 1
        # the area that can be trapped is z = min(height[i], height[j]) then the area is for k in range(i + 1, j): area += z - height[k]

        def calcArea(i, j):
            z = min(height[i], height[j])
            area = 0

            for k in range(i + 1, j): 
                if (z - height[k]) < 0: return 0

                area += z - height[k]

            return area

        i, j = 0, 1
        area_sum = 0
        max_area = 0
        max_sum = 0

        # i feel like we want them to start at the beginning, then the gap get bigger. we then reset the gap, moving i to j and then incrementing j again
        # we reset when height[j] < height[j+1] and height[j] > height[i] (because this then has a spike in the middle)

        while j < len(height) and i < len(height) - 1:
            area = calcArea(i, j)
            # print(i, j, area)

            if height[i] == 0:
                i += 1
                j += 1
                continue

            if area > max_area:
                max_area = area

            if height[j - 1] > height[j] and height[j - 1] > height[i]:
                i = j - 1
                area_sum += max_area
                max_area = 0
            else:
                j += 1

            if j == len(height):
                i += 1
                j = i + 1
                area_sum += max_area

                if area_sum > max_sum:
                    # print("assiginging max _cum", area_sum)
                    max_sum = area_sum
                    max_area = 0
                    area_sum = 0


        return max_sum

        
