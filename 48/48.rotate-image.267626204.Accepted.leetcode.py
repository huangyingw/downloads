class Solution:
    def rotate(self, matrix):
        matrix[::] = list(zip(*matrix[::-1]))

