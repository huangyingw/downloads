class Solution(object):
    def flipAndInvertImage(self, A):
        Ans = []
        for a in A:
            LEN = len(a)
            row = []
            for i in range(LEN):
                row.append([1, 0][a[LEN - 1 - i]])
            Ans.append(row)
        return Ans

