class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        super_ugly = [1]
        indices = [0 for _ in range(len(primes))]
        candidates = primes[:]
        while len(super_ugly) < n:
            ugly = min(candidates)
            super_ugly.append(ugly)
            for i in range(len(candidates)):
                if ugly == candidates[i]:
                    indices[i] += 1
                    candidates[i] = primes[i] * super_ugly[indices[i]]
        return super_ugly[-1]

