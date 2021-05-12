class Solution:
    def firstUniqChar(self, s):
        res = []
        ret = len(s)
        for i in set(s):
            if s.count(i) == 1:
                res.append(i)
        if not res:
            return -1
        for i in res:
            ret = min(ret, s.index(i))
        return ret

