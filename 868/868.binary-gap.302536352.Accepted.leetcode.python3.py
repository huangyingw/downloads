class Solution:
    def binaryGap(self, N):
        n = str(bin(N))
        count = 0
        last = n.index('1')
        for i in range(last + 1, len(n)):
            if n[i] == '1':
                if count < i - last:
                    count = i - last
                last = i
        return count

