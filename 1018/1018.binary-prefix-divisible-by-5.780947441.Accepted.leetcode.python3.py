class Solution(object):
    def prefixesDivBy5(self, A):
        result = []
        num = 0
        for bit in A:
            num = (num * 2 + bit) % 5
            result.append(num == 0)
        return result

