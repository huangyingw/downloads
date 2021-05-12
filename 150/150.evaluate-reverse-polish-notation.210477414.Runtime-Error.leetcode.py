class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token.equals("+"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token.equals("-"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token.equals("*"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token.equals("/"):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 / num2)
            else:
                stack.append(int(token))
        return stack.pop()

