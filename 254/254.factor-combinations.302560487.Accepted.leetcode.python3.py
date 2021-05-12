class Solution(object):
    def getFactors(self, n):
        stack = [(n, 2, [])]
        factors = []
        while stack:
            num, trial, partial = stack.pop()
            while trial * trial <= num:
                if num % trial == 0:
                    factors.append(partial + [num // trial, trial])
                    stack.append((num // trial, trial, partial + [trial]))
                trial += 1
        return factors

