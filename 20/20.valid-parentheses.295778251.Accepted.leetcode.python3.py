class Solution:
    def isValid(self, s: str) -> bool:
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
        return len(stack) == 0

