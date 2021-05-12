class Solution:
    def findTheDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

