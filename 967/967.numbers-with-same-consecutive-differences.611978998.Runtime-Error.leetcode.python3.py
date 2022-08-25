class Solution(object):
    def numsSameConsecDiff(self, N, K):
        if N == 1:
            return [0]
        partials = [i for i in range(1, 10)]
        for _ in range(N - 1):
            new_partials = []
            for p in partials:
                last_digit = [p % 10 - K, p % 10 - K]
                if 0 <= last_digit <= 9:
                    new_partials.append(p * 10 + last_digit)
            partials = new_partials
        return partials

