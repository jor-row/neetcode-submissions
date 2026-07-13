class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        visited = set()

        def dfs(i, j):
            print(i, j)

            if (i, j) in visited or i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != target:
                return

            visited.add((i, j))

            image[i][j] = color

            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        dfs(sr, sc)

        return image



        