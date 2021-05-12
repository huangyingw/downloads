class Solution:
    def isValid(self, s):
        if s is None:
            return True
        stack = []
        for t in s:
            if t == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif t == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                stack.append(t)
        return not stack

