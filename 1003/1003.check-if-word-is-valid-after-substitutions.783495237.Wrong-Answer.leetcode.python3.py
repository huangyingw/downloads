class Solution(object):
    def isValid(self, S):
        stack = []
        if not S:
            return False
        for char in S:
            if char == 'a':
                stack.append('a')
            if char == 'b':
                if not stack:
                    return False
                if stack[-1] == 'a':
                    stack.pop()
                    stack.append(char)
                    print("stack --> %s" % stack)
            if char == 'c':
                if not stack:
                    return False
                if stack[-1] == 'b':
                    stack.pop()
                    print("stack --> %s" % stack)
        return len(stack) == 0

