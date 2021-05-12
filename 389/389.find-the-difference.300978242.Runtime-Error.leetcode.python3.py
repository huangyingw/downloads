class Solution:
    def findTheDifference(self, s, t):
        s_count, t_count = Counter(s), Counter(t)
        for k, v in t_count.items():
            if k not in s_count:
                return k
            if v > s_count[k]:
                return k

