class Solution:
    def shiftingLetters(self, S, shifts):
        temp = list(S)
        length = len(shifts)
        offset = 0
        for i in range(length - 1, -1, -1):
            offset += shifts[i]
            offset %= 26
            temp[i] = chr(ord(temp[i]) + offset if ord(temp[i]) + offset <= 122 else ord(temp[i]) + offset - 26)
        return ''.join(temp)

