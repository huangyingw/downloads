class Solution(object):
    def findRepeatedDnaSequences(self, s):
        result = set()
        vset = set()

        for index in range(10, len(s) + 1):
            substr = s[index - 10:index]

            if substr in vset:
                result.append(substr)
            else:
                vset.append(substr)
        return list(result)

