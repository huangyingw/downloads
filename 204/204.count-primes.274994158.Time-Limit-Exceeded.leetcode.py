class Solution:
    def countPrimes(self, n):
        def isPrime(num):
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        if n < 3:
            return 0
        count = 1
        for i in range(3, n, 2):
            if isPrime(i):
                count += 1
        return count

