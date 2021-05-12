class Solution:
    def wordSubsets(self, A, B):
        ccb = {}
        for b in B:
            cb = {}
            for l in b:
                if l in cb:
                    cb[l] += 1
                else:
                    cb[l] = 1
            for l in b:
                if l not in ccb or ccb[l] < cb[l]:
                    ccb[l] = cb[l]
        ans = []
        for a in A:
            flag = True
            for i in ccb:
                if a.count(i) < ccb[i]:
                    flag = False
                    break
            if flag:
                ans.append(a)
        return ans

