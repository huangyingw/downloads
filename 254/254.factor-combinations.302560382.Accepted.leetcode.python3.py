class Solution(object):
    def getFactors(self, n):
        return self.factorise(n, 2, [], [])

    def factorise(self, n, trial, partial, factors):
        while trial * trial <= n:
            if n % trial == 0:
                factors.append(partial + [n // trial, trial])
                self.factorise(n // trial, trial, partial + [trial], factors)
            trial += 1
        return factors

