class Solution(object):
    def sortArrayByParity(self, A):
        Ans = []
        for a in A:
            if a % 2:
                Ans.append(a)
            else:
                Ans.insert(0, a)
        return Ans

