class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = set()
        for cs, ct in zip(s, t):
            if cs in sMap:
                if sMap[cs] != ct:
                    return False
            elif ct in tMap:
                return False
            sMap[cs] = ct
            tMap.add(ct)
        return True

