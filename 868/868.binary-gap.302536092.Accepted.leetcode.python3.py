class Solution:
    def binaryGap(self, N):
        temp = bin(N)
        if temp.count('1') <= 1:
            return 0
        return len(max(bin(N)[2:].split('1')[1:-1], key=len)) + 1

