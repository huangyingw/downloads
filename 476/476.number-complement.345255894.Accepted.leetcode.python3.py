class Solution(object):
    def findComplement(self, num):
        mask = ~0
        while num & mask:
            mask = mask << 1
        return ~num ^ mask

