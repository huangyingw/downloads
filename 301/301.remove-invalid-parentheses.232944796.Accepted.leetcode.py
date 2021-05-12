class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s:
            return ['']
        q = {s}
        while q:
            ans = filter(self.isValidParentheses, q)
            if ans:
                return ans
            q = {cur[:i] + cur[i + 1:] for cur in q for i in xrange(len(cur))}

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0

