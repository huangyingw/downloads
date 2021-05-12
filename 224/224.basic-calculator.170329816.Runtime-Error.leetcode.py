class Solution(object):
    def calculate(self, s):
        result, idx = 0, 0
        stack = [1, 1]

        while idx < len(s):
            if s[idx].isdigit():
                num = ord(s[idx]) - ord('0')

                while idx + 1 < len(s) and s[idx + 1].isdigit():
                    num = num * 10 + ord(s[idx + 1]) - ord('0')
                    idx += 1

                result += stack.pop() * num
            elif s[idx] in ['(', '+']:
                stack.append(stack[-1])
            elif s[idx] == ')':
                stack.pop()
            elif s[idx] == '-':
                stack.append(-1 * stack[-1])

        return result

