from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        results = []
        freq = list(Counter(candidates).items())
        self.combos(freq, 0, target, [], results)
        return results

    def combos(self, freq, next, target, partial, results):
        if target == 0:
            results.append(partial)
            return
        if next == len(freq):
            return
        for i in range(freq[next][1] + 1):
            if i * freq[next][0] > target:
                break
            self.combos(freq, next + 1, target - i * freq[next][0], partial + [freq[next][0]] * i, results)

