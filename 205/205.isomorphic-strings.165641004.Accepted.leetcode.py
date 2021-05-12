class Solution(object):
    def isIsomorphic(self, s, t):
        sMap = {}
        tMap = {}

        for idx in range(len(s)):
            targe = sMap.get(s[idx], None)
            source = tMap.get(t[idx], None)

            if not source and not targe:
                sMap[s[idx]] = t[idx]
                tMap[t[idx]] = s[idx]
            elif s[idx] != source or t[idx] != targe:
                return False
        return True

