class Solution:
    def findTheDifference(self, s, t):
        xr = 0
        for c in s:
            xr = xr ^ ord(c)
        for c in t:
            xr = xr ^ ord(c)
        return chr(xr)

