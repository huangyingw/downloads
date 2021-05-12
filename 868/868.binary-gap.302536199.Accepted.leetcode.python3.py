class Solution:
    def binaryGap(self, N):
        max = 0
        str = bin(N)[2:]
        lst = []
        for i in range(len(str)):
            if int(str[i]) == 1:
                lst.append(i)
        if len(lst) < 2:
            return 0
        for i in range(len(lst)):
            if max < lst[i] - lst[i - 1]:
                max = lst[i] - lst[i - 1]
        return max

