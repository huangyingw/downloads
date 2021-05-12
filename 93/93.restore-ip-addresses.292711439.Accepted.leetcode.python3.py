class Solution(object):
    def restoreIpAddresses(self, s):
        ls = len(s)
        if ls == 0 or ls > 12:
            return []
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    m = ls - i - j - k
                    if m > 0 and m <= 3:
                        add1 = s[0:i]
                        add2 = s[i:i + j]
                        add3 = s[i + j:i + j + k]
                        add4 = s[i + j + k:]
                        if self.isValid(add1) and self.isValid(add2) and \
                                self.isValid(add3) and self.isValid(add4):
                            res.append(add1 + '.' + add2 + '.' + add3 + '.' + add4)
        return res

    def isValid(self, add):
        if len(add) == 1:
            return True
        if add[0] == '0':
            return False
        if int(add) <= 255:
            return True
        return False

