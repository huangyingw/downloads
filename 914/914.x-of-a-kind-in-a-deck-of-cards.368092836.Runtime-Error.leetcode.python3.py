class Solution:
    def hasGroupsSizeX(self, deck):

        from collections import Counter
        from functools import reduce

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        count = Counter(deck).values()
        return reduce(gcd, count) >= 2

    def hasGroupsSizeX(self, deck):
        return reduce(fractions.gcd, collections.Counter(deck).values()) > 1

