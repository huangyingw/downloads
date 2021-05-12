class Solution(object):
    def isHappy(self, n):
        seen_numbers = set()
        while n not in seen_numbers:
            seen_numbers.add(n)
            n = sum(map(lambda x: int(x) * int(x), list(str(n))))
        return n == 1

