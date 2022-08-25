class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result += [[1] * (i + 1)]
            print("i --> %s" % i)
            print("result[i - 1] --> %s" % result[i - 1])
            print("result[i] --> %s" % result[i])
            for j in range(0, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

