class Solution(object):
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        queue = []

        for token in tokens:
            if token not in operators:
                queue.append(int(token))
            elif token == '+':
                num1 = queue.pop(0)
                num2 = queue.pop(0)
                queue.append(num1 + num2)
            elif token == '*':
                num1 = queue.pop(0)
                num2 = queue.pop(0)
                queue.append(num1 * num2)
            elif token == '/':
                num1 = queue.pop(0)
                num2 = queue.pop(0)
                queue.append(num1 / num2)

        return queue.pop(0)

