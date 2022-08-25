class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    left = stack.pop()
                    print("left --> %s" % left)
                    print("num --> %s" % num)
                    stack.append(left // num)
                    print("stack --> %s" % stack)
                    if left // num < 0:
                        stack[-1] += 1

                num = 0
                op = c
        return sum(stack)

