class Solution(object):

    def strobogrammatic_helper(self, m, n):
        if m == 0:
            return []

        if m == 1:
            return ['0', '1', '8']

        temp = self.strobogrammatic_helper(m - 2, n)
        result = []

        if not temp:
            result.append('11')
            result.append('69')
            result.append('88')
            result.append('96')
            if m != n:
                result.append('00')

        for t in temp:
            result.append('1' + t + '1')
            result.append('6' + t + '9')
            result.append('8' + t + '8')
            result.append('9' + t + '6')
            if m != n:
                result.append('0' + t + '0')

        return result

    def strobogrammatic(self, n):
        return self.strobogrammatic_helper(n, n)

