class Solution:
    def fairCandySwap(self, A, B):
        sb = set(B)
        diff = (sum(B) - sum(A)) // 2
        for num in A:
            if num + diff in sb:
                return num, num + diff

