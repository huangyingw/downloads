class Solution(object):
    def findRepeatedDnaSequences(self, s):
        result = set()
        vset = set()

        for index in range(10, len(s) + 1):
            substr = s[index - 10:index]

            if substr in vset:
                result.add(substr)
            else:
                vset.add(substr)
        return list(result)

