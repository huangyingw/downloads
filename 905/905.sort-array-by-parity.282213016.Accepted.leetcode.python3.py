class Solution(object):
    def sortArrayByParity(self, A):
        even, odd = [], []
        for a in A:
            if a % 2:
                odd.append(a)
            else:
                even.append(a)
        return even + odd

