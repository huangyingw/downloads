class Solution(object):
    def removeInvalidParentheses(self, s):
        def isValid(s):
            a = 0
            for c in s:
                a += {'(': 1, ')': -1}.get(c, 0)
                if a < 0:
                    return False
            return a == 0

        visited = set([s])
        ans = []
        queue = collections.deque([s])
        done = False
        while queue:
            t = queue.popleft()
            if isValid(t):
                done = True
                ans.append(t)
            if done:
                continue
            for x in range(len(t)):
                if t[x] not in ('(', ')'):
                    continue
                ns = t[:x] + t[x + 1:]
                if ns not in visited:
                    visited.add(ns)
                    queue.append(ns)

        return ans
1

