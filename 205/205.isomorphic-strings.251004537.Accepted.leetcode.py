class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        ls = len(s)
        sMap = [0] * 127
        tMap = [0] * 127
        for i in range(ls):
            s_num, t_num = ord(s[i]), ord(t[i])
            if sMap[s_num] == 0 and tMap[t_num] == 0:
                sMap[s_num] = t_num
                tMap[t_num] = s_num
            elif tMap[t_num] != s_num or sMap[s_num] != t_num:
                return False
        return True

