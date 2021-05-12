class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            if i <= 1:
                pre = [1] * (i + 1)
                result.append(pre)
            else:
                temp = [1]
                for y in range(1, i):
                    temp.append(pre[y - 1] + pre[y])
                pre = temp + [1]
                result.append(pre)
        return result

