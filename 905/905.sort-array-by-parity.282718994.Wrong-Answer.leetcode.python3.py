class Solution(object):
    def sortArrayByParity(self, A):
        return A.sort(key=lambda a: a % 2)

