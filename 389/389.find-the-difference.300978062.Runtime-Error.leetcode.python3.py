class Solution:
    def findTheDifference(self, s, t):
        return (set(t) - set(s)).pop()

