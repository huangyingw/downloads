class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.findCombination(result, [], candidates, target)
        return result

    def findCombination(self, result, path, candidates, target):
        if target == 0:
            result.append(path.copy())
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            if i - 1 >= 0 and candidates[i - 1] == candidates[i]:
                continue
            self.findCombination(result, path + [candidates[i]], candidates[i + 1:], target - candidates[i])

