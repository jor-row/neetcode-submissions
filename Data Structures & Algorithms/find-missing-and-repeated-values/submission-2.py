class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}

        i = 0
        j = 0

        while i < len(grid):
            j = 0

            while j < len(grid[0]):

                num = grid[i][j]

                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1

                j += 1

            i += 1


        res = [-1, -1]

        for i in range(1, len(grid)**2 + 1):
            if i not in count:
                res[1] = i
            elif count[i] == 2:
                res[0] = i


        return res
        