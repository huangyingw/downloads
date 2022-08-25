class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
                print("num --> %s" % num)
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                    print("stack --> %s" % stack)
                elif op == '-':
                    stack.append(-num)
                    print("stack --> %s" % stack)
                elif op == '*':
                    stack.append(stack.pop() * num)
                    print("stack --> %s" % stack)
                else:
                    left = stack.pop()
                    stack.append(left // num)
                    print("stack --> %s" % stack)
                    if left // num < 0 and left % num != 0:
                        stack[-1] += 1
                num = 0
                op = c
        return sum(stack)

