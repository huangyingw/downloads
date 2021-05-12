class Solution:
    def reverseOnlyLetters(self, S):
        temp = list(S)
        left = 0
        right = len(temp) - 1
        while left < right:
            while left < right and not temp[left].isalpha():
                left += 1
            while left < right and not temp[right].isalpha():
                right -= 1
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        return ''.join(temp)

