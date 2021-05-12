from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)])
        for i in range(len(p), len(s)):
            if sCounter == pCounter:
                res.append(i - len(p))
            sCounter[s[i]] += 1
            sCounter[s[i - len(p) + 1]] -= 1
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]
        return res

