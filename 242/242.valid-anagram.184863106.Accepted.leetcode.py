class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        charCount = {}
        for idx in range(len(s)):
            if s[idx] not in charCount:
                charCount[s[idx]] = 0

            if t[idx] not in charCount:
                charCount[t[idx]] = 0

            charCount[s[idx]] += 1
            charCount[t[idx]] -= 1

        for char in charCount:
            if charCount[char] != 0:
                return False

        return True

