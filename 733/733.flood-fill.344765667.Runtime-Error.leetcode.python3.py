class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c, R, C):
            if r < 0 or r >= R or c < 0 or c >= C or image[r][c] != color:
                return
            image[r][c] = newColor
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        dfs(sr, sc)
        return image

