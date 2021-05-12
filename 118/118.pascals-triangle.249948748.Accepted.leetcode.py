class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            result += [[1]]
            for num1, num2 in zip(result[-2][:-1], result[-2][1:]):
                result[-1].append(num1 + num2)
            result[-1] += [1]
        return result

