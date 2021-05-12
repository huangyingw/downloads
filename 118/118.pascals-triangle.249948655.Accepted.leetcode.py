class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        result = []
        result.append([1])
        for i in range(1, numRows):
            result.append([])
            a = 1
            result[i].append(1)
            while a < i:
                result[i].append(result[i - 1][a - 1] + result[i - 1][a])
                a += 1
            result[i].append(1)
        return result

