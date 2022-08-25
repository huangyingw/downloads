class Solution(object):
    def calculate(self, s):
        result, idx, num = 0, 0, 0
        stack = [1, 1]
        while idx < len(s):
            if s[idx].isdigit():
                num = num * 10 + ord(s[idx]) - ord('0')
                if idx + 1 == len(s) or not s[idx + 1].isdigit():
                    result += stack.pop() * num
            else:
                print("stack --> %s" % stack)
                num = 0
                if s[idx] in ['(', '+']:
                    print("stack --> %s" % stack)
                    stack.append(stack[-1])
                elif s[idx] == ')':
                    stack.pop()
                    print("stack --> %s" % stack)
                elif s[idx] == '-':
                    stack.append(-1 * stack[-1])
            idx += 1
        return result

