class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if (len(s1) + len(s2) != len(s3)):
            return False

        s1 = '0' + s1
        s2 = '0' + s2
        s3 = '0' + s3

        def dfs(row, col):
            if row == len(s1) or col == len(s2):
                return False

            if (s1[row] != s3[row + col] and s2[col] != s3[row + col]):
                return False

            if (row + 1 == len(s1) and col + 1 == len(s2)):
                return True

            return dfs(row + 1, col) or dfs(row, col + 1)
        return dfs(0, 0)

