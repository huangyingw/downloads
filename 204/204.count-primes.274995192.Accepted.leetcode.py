class Solution(object):
    def countPrimes(self, n):
        isPrime = [True] * n
        i = 2
        while i * i <= n:
            if isPrime[i]:
                for j in xrange(i * i, n, i):
                    isPrime[j] = False
            i += 1
        count = 0
        for i in xrange(2, n):
            if isPrime[i]:
                count += 1
        return count

