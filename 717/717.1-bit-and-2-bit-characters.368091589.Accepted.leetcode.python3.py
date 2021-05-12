class Solution:

    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0

