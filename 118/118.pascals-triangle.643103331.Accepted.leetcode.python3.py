class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result += [[1] * (i + 1)]
            for j in range(1, i):
                print("result[i - 1] --> %s" % result[i - 1])
                print("i --> %s" % i)
                print("j --> %s" % j)
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
            print("result[i] --> %s" % result[i])
        return result

