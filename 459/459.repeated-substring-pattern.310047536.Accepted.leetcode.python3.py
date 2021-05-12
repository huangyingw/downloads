"""
1. First char of input string is first char of repeated substring
2. Last char of input string is last char of repeated substring
3. Let S1 = S + S (where S in input string)
4. Remove 1 and last char of S1. Let this be S2
5. If S exists in S2 then return true else false
6. Let i be index in S2 where S starts then repeated substring length i + 1 and 
repeated substring S[0: i+1]
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


class SolutionKMP:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, j, l = 1, 0, len(s)
        lookup = [0] * (l + 1)
        while i < l:
            if s[i] == s[j]:
                i += 1
                j += 1
                lookup[i] = j
            elif j == 0:
                i += 1
            else:
                j = lookup[j]
        return lookup[l] and not lookup[l] % (l - lookup[l])

