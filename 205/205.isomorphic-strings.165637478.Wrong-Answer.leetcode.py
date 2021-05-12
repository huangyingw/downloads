class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for idx in range(len(s)):
            if s_to_t.get(s[idx], s[idx]) != t[idx] or t_to_s.get(t[idx], t[idx]) != s[idx]:
                return False

            s_to_t[s[idx]] = t[idx]
            t_to_s[t[idx]] = s[idx]
        return True

