class Solution:
    def checkValidString(self, s):
        cmin = cmax = 0
        for i in s:
            cmax = cmax - 1 if i == ')' else cmax + 1
            cmin = cmin + 1 if i == '(' else max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

