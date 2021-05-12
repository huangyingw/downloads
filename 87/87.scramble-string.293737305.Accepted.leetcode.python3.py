class Solution(object):
    def __init__(self):
        self.cache = {}

    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        if s1 + s2 in self.cache:
            return self.cache[s1 + s2]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.cache[s1 + s2] = False
            return False
        for index in range(1, len(s1)):
            if self.isScramble(s1[:index], s2[:index]) and self.isScramble(s1[index:], s2[index:]):
                self.cache[s1 + s2] = True
                return True
            if self.isScramble(s1[:index], s2[-index:]) and self.isScramble(s1[index:], s2[0:-index]):
                self.cache[s1 + s2] = True
                return True
        self.cache[s1 + s2] = False
        return False

