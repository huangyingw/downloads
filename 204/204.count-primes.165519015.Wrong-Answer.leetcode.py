class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        primes = [True] * (n + 1)
        primes[1] = False
        i = 2

        while i * i <= n:
            if primes[i]:
                for j in range(2 * i, n + 1, i):
                    print('j --> %s' % j)
                    primes[j] = False
            i += 1
            print('i --> %s' % i)
        count = 0

        for prime in primes:
            if prime:
                count += 1
        return count

