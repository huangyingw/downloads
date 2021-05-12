class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            print('i --> %s' % (i))
            result += [[1] * (i + 1)]
            print('result --> %s' % (result))
            for j in range(1, i):
                print('j --> %s' % (j))
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
                print('result[i][j] --> %s' % (result[i][j]))
                print
            print
        return result

