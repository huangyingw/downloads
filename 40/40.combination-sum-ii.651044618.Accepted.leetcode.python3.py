class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.findCombination(result, [], 0, candidates, target)
        return result

    def findCombination(self, result, path, start, candidates, target):
        if target == 0:
            result.append(path.copy())
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i - 1 >= start and candidates[i] == candidates[i - 1]:
                continue
            self.findCombination(result, path + [candidates[i]], i + 1, candidates, target - candidates[i])

