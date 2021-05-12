class Solution:
    def findTheDifference(self, s, t):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(c) != t.count(c):
                return c

