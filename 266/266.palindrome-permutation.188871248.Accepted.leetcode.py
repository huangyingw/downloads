class Solution(object):
    def canPermutePalindrome(self, s):
        charCount = {}

        for idx in range(len(s)):
            if s[idx] not in charCount:
                charCount[s[idx]] = 0

            charCount[s[idx]] += 1

        tolerance = 0

        for char in charCount:
            if charCount[char] % 2 != 0:
                tolerance += 1

        if len(s) % 2 != 0:
            return tolerance == 1
        else:
            return tolerance == 0

