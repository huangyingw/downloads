class Solution:
    def flipAndInvertImage(self, A):
        reverse = []
        for i in A:
            temp = []
            for j in reversed(i):
                if(j == 0):
                    temp.append(1)
                else:
                    temp.append(0)
            reverse.append(temp)
        return (reverse)

