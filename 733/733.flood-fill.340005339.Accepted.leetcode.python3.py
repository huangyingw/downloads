class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def dfs(i, j):
            if image[i][j] == color:
                image[i][j] = newColor
                if i >= 1:
                    dfs(i - 1, j)
                if j >= 1:
                    dfs(i, j - 1)
                if i < m - 1:
                    dfs(i + 1, j)
                if j < n - 1:
                    dfs(i, j + 1)

        dfs(sr, sc)
        return image

