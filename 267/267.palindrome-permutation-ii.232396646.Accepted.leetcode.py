class Solution(object):
    def __init__(self):
        self.results = []

    def generatePalindromes(self, s):
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        already, candidate, single = False, "", ""

        for i in d:
            num = d[i] / 2
            for j in range(num):
                candidate += i
            if d[i] % 2 != 0:
                if already:
                    return []
                else:
                    already = True
                    single += i

        if len(candidate) == 0 and len(single) != 0:
            self.results.append(single)
            return self.results

        for i in range(len(candidate)):
            if i > 0 and candidate[i] == candidate[i - 1]:
                continue
            self.recursion(candidate[i], candidate[:i] + candidate[i + 1:], len(candidate), single)

        return self.results

    def recursion(self, left, candidate, l, single):
        if len(left) == l:
            self.results.append(left + single + left[::-1])
            return
        for i in range(len(candidate)):
            if i > 0 and candidate[i] == candidate[i - 1]:
                continue
            self.recursion(left + candidate[i], candidate[:i] + candidate[i + 1:], l, single)

