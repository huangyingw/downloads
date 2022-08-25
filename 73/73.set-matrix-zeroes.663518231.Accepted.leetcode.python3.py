class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        is_col= False
        for i in range(row):
            if matrix[i][0] == 0:
                is_col= True
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,row):
            for j in range(1,col):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
        if is_col:
            for i in range(row):
                matrix[i][0] = 0

