class Solution(object):

    def findReplaceString(self, S, indexes, sources, targets):

        listOfS = list(S)
        distance = 0
        for index, source, target in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i + len(s)] == s:
                listOfS[index:index + len(source)] = target
        return "".join(listOfS)

    def findReplaceString2(self, S, indexes, sources, targets):
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S

