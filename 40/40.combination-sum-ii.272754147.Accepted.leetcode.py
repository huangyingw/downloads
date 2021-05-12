from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        results = []
        partials = [[]]
        freq = list(Counter(candidates).items())
        for candidate, count in freq:
            new_partials = []
            for partial in partials:
                partial_sum = sum(partial)
                for i in range(count + 1):
                    if partial_sum + candidate * i < target:
                        new_partials.append(partial + [candidate] * i)
                    elif partial_sum + candidate * i == target:
                        results.append(partial + [candidate] * i)
                    if partial_sum + candidate * i >= target:
                        break
            partials = new_partials
        return results

