class Solution(object):
    def freqAlphabets(self, s):

        result = []
        n = len(s)
        i = 0
        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                result.append(chr(int(s[i:i + 2]) + ord("a") - 1))
                i += 3
            else:
                result.append(chr(int(s[i]) + ord("a") - 1))
                i += 1
        return "".join(result)

