class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # area = min(heights[i], heights[j]) * (j - i) where j is to the left of i

        # two pointer approach, 

        # max_area = 0

        # for i in range(len(heights) - 1):
        #     for j in range(i + 1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j - i)

        #         if area > max_area:
        #             max_area = area

        # return max_area

        i, j = 0, len(heights) - 1
        max_area = 0

        while i < j:
            area = min(heights[i], heights[j]) * (j - i)

            if area > max_area:
                max_area = area

            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1

        return max_area

        