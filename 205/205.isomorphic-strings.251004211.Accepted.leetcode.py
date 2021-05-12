class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}
        for idx in range(len(s)):
            if s[idx] in sMap and sMap[s[idx]] != t[idx]:
                return False
            if t[idx] in tMap and tMap[t[idx]] != s[idx]:
                return False
            sMap[s[idx]] = t[idx]
            tMap[t[idx]] = s[idx]
        return True

