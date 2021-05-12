class Solution(object):
    def calculate(self, s):
        result, idx, num = 0, 0, 0
        stack = [1, 1]

        for idx, val in enumerate(s):
            if val.isdigit():
                num = num * 10 + ord(val) - ord('0')

                if idx + 1 == len(s) or not s[idx + 1].isdigit():
                    result += stack.pop() * num
            else:
                num = 0

                if val in ['(', '+']:
                    stack.append(stack[-1])
                elif val == ')':
                    stack.pop()
                elif val == '-':
                    stack.append(-1 * stack[-1])

        return result

