class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
                print("num --> %s" % num)
            if (not c.isdigit() or c != ' ') or i == len(s) - 1:
                print("op --> %s" % op)
                if op == '+':
                    stack.append(num)
                    print("stack --> 1 %s" % stack)
                elif op == '-':
                    stack.append(-num)
                    print("stack --> 2 %s" % stack)
                elif op == '*':
                    stack.append(stack.pop() * num)
                    print("stack --> 3 %s" % stack)
                else:
                    left = stack.pop()
                    stack.append(left // num)
                    print("stack --> 4 %s" % stack)
                    if left // num < 0 and left % num != 0:
                        stack[-1] += 1
                num = 0
                op = c
        return sum(stack)

