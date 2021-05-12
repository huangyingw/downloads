import string


class Solution:
    def reverseOnlyLetters(self, S):
        letters = set(string.ascii_lowercase + string.ascii_uppercase)
        S = [c for c in S]
        left, right = 0, len(S) - 1
        while left < right:
            while left < right and S[left] not in letters:
                left += 1
            while left < right and S[right] not in letters:
                right -= 1
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
        return "".join(S)

