class Solution_sort(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda a: a % 2)
        return A

