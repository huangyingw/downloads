class Solution(object):
    def addOperators(self, num, target):
        def isLeadingZeros(num):
            return num.startswith('00') or int(num) and num.startswith('0')

        def solve(num, target, mulExpr='', mulVal=1):
            ans = []
            # remove leading zeros
            if isLeadingZeros(num):
                pass
            elif int(num) * mulVal == target:
                ans += num + mulExpr,
            for x in range(len(num) - 1):
                lnum, rnum = num[:x + 1], num[x + 1:]
                # remove leading zeros
                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                #op = '+'
                for left in solve(lnum, target - rightVal):
                    ans += left + '+' + right,
                #op = '-'
                for left in solve(lnum, target + rightVal):
                    ans += left + '-' + right,
                #op = '*'
                for left in solve(lnum, target, '*' + right, rightVal):
                    ans += left,
            return ans
        if not num:
            return []
        return solve(num, target)

