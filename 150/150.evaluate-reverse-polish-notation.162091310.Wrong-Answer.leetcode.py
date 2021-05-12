class Solution(object):
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)

        return stack.pop()

