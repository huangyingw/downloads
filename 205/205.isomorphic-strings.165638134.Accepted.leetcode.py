class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for idx in range(len(s)):
            if s[idx] in s_to_t and s_to_t[s[idx]] != t[idx]:
                return False

            if t[idx] in t_to_s and t_to_s[t[idx]] != s[idx]:
                return False

            s_to_t[s[idx]] = t[idx]
            t_to_s[t[idx]] = s[idx]
        return True

