class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = L + ((R - L) >> 1)
            if self.search_lower_than_mid(matrix, n, mid) < k:
                L = mid + 1
            else:
                R = mid
        return L

    def search_lower_than_mid(self, matrix, n, mid):
        x, y = n - 1, 0
        cnt = 0
        while x >= 0 and y < n:
            if matrix[x][y] <= mid:
                y += 1
                cnt += x + 1
            else:
                x -= 1
        return cnt

