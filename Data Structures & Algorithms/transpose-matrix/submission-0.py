class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = []

        for j in range(len(matrix[0])):
            new = []
            for i in range(len(matrix)):
                new.append(matrix[i][j])

            trans.append(new)

        return trans

        