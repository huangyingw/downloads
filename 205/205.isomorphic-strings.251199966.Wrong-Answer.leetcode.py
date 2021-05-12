class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}
        for idx in range(len(s)):
            if s[idx] not in sMap:
                sMap[s[idx]] = t[idx]
            elif sMap[s[idx]] != t[idx]:
                return False
            elif t[idx] not in tMap:
                tMap[t[idx]] = s[idx]
            elif tMap[t[idx]] != s[idx]:
                return False
        return True

