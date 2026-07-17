class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[] for i in range(rowIndex+1)]
        print(rows)
        rows[0] = [1]


        for i in range(1, rowIndex + 1):
            prev = rows[i - 1]

            new_mid = []

            for j in range(len(prev)-1):
                new_mid.append(prev[j] + prev[j+1])


            rows[i] = [1] + new_mid + [1]

        return rows[-1]

        