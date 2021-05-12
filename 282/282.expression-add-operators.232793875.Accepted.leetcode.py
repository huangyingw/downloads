class Solution(object):
    def addOperators(self, num, target):
        def solve(target, pos, negate, prod):
            expr = []

            for i in xrange(pos, len(num)):
                if i != pos and num[pos] == "0":
                    break

                if i == len(num) - 1:
                    if negate * prod * int(num[pos:i + 1]) == target:
                        expr.extend([num[pos:i + 1]])
                    break

                add_expr = solve(target - prod * negate * long(num[pos:i + 1]), i + 1, 1, 1)
                expr.extend([num[pos:i + 1] + "+" + e for e in add_expr])

                sub_expr = solve(target - prod * negate * long(num[pos:i + 1]), i + 1, -1, 1)
                expr.extend([num[pos:i + 1] + "-" + e for e in sub_expr])

                mul_expr = solve(target, i + 1, 1, prod * negate * long(num[pos:i + 1]))
                expr.extend([num[pos:i + 1] + "*" + e for e in mul_expr])

            return expr

        return solve(target, 0, 1, 1)

