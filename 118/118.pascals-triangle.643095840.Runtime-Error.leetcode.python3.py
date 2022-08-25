class Solution(object):
    def generate(self, numRows):
        result = [1]
        for i in range(numRows):
            result += [[1] * i]
            for j in range(1, i - 1):
                print("result[i - 1] --> %s" % result[i - 1])
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

