class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                print("num1 + num2 --> %s" % (num1 + num2))
                stack.append(num1 + num2)
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                print("num1 - num2 --> %s" % (num1 - num2))
                stack.append(num1 - num2)
            elif token == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                print("num1 * num2 --> %s" % (num1 * num2))
                stack.append(num1 * num2)
            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                print("num1 / num2 --> %s" % (num1 / num2))
                stack.append(num1 / num2)
            else:
                print("token --> %s" % (token))
                stack.append(int(token))
        return stack.pop()

