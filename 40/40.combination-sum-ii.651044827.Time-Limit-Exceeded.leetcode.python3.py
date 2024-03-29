class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    if len(temp) > 0 and temp[-1] >= j:
                        continue
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check = {}
        for temp in dp[target]:
            value = [candidates[t] for t in temp]
            try:
                check[str(value)] += 1
            except KeyError:
                check[str(value)] = 1
                res.append(value)
        return res

