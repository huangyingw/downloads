class Solution:
    def fairCandySwap(self, A, B):
        sum_A = sum(A)
        sum_B = sum(B)
        diff = sum_A - sum_B
        for i in set(A):
            if i - diff // 2 in set(B):
                return [i, i - diff // 2]

