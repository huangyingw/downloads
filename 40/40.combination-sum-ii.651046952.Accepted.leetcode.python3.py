class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList)
                return
            previous = -1
            for start in range(index, len(candidates)):
                if previous != candidates[start]:
                    recursive(candidates, target - candidates[start], currList + [candidates[start]], start + 1)
                    previous = candidates[start]
        recursive(candidates, target, [], 0)
        return result

