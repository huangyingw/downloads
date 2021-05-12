class Solution:
    def decodeString(self, s):
        stack = []
        n = 0
        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c == '[':
                stack.append(n)
                n = 0
            elif c.isalpha():
                stack.append(c)
            elif c == ']':
                ss = self.popStack(stack)
                for i in range(stack.pop()):
                    stack.append(ss)
        return self.popStack(stack)

    def popStack(self, stack):
        result = ''
        while stack and type(stack[-1]) is not int:
            result = stack.pop() + result
        return result

