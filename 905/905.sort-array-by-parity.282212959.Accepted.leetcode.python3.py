class Solution(object):
    def sortArrayByParity(self, A):
        Ans = [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
        return Ans

