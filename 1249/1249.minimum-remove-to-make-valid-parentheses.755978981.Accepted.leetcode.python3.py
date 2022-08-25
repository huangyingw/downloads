class Solution(object):
    def minRemoveToMakeValid(self, s):
        opening = []
        removals = set()
        for i, c in enumerate(s):
            if c == "(":
                opening.append(i)
            elif c == ")":
                if not opening:
                    removals.add(i)
                else:
                    opening.pop()
        removals.update(opening)
        return "".join(c for i, c in enumerate(s) if i not in removals)

