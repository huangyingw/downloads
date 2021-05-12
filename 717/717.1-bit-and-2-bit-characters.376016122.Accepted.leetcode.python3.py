class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pos = 0

        while pos < len(bits) - 1:

            pos += bits[pos] + 1
        return pos == len(bits) - 1

