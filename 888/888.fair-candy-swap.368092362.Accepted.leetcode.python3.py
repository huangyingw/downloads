class Solution:

    def fairCandySwap(self, A, B):

        sum_A = sum(A)
        sum_B = sum(B)
        diff = sum_A - sum_B
        for i in set(A):
            if i - diff // 2 in set(B):
                return [i, i - diff // 2]

    def fairCandySwap(self, A, B):

        sb = set(B)
        diff = (sum(B) - sum(A)) // 2
        for num in A:
            if num + diff in sb:
                return num, num + diff

