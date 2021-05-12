class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

