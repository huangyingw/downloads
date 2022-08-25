class Solution(object):
    def evalRPN(self, tokens):
        ops = {'+', '-', '/', '*'}
        stack = []
        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                if token == '/':
                    stack.append(int(left // float(right)))
                else:
                    stack.append((eval(str(left) + token + str(right))))
            else:
                stack.append(int(token))
        return stack[-1]

