class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            print("c --> %s" % c)
            if c.isdigit():
                num = num * 10 + int(c)
                print("num --> %s" % num)
            elif (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    print("stack --> %s" % stack)
                    print("num --> %s" % num)
                    stack.append(stack.pop() * num)
                else:
                    left = stack.pop()
                    print("left --> %s" % left)
                    print("stack.append --> %s" % (left // num))
                    stack.append(left // num)
                    if left // num < 0 and left % num != 0:
                        stack[-1] += 1
                num = 0
                op = c
        return sum(stack)

