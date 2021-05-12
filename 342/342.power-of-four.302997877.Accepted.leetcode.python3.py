class Solution(object):
    def isPowerOfFour(self, num):
        bin_num = bin(num)[2:]
        c = bin_num.count('0')
        return bin_num[0] == '1' and c == len(bin_num) - 1 and c % 2 == 0

