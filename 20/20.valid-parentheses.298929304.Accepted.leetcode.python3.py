class Solution:
    def isValid(self, s: str):
        stack = []
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in d.values():
                stack.append(c)
            elif (not stack) or (stack.pop() != d[c]):
                return False
        return not stack

