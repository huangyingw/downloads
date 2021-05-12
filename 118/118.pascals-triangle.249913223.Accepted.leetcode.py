class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        Ans = []
        Ans.append([1])
        for i in range(1, numRows):
            Ans.append([])
            a = 1
            Ans[i].append(1)
            while a < i:
                Ans[i].append(Ans[i - 1][a - 1] + Ans[i - 1][a])
                a += 1
            Ans[i].append(1)
        return Ans

