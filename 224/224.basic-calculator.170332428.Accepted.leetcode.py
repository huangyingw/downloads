class Solution(object):
    def calculate(self, s):
        result, idx, num = 0, 0, 0
        stack = [1, 1]

        while idx < len(s):
            if s[idx].isdigit():
                num = num * 10 + ord(s[idx]) - ord('0')
                idx += 1

                if idx == len(s) or not s[idx].isdigit():
                    result += stack.pop() * num
                    num = 0

                continue
            elif s[idx] in ['(', '+']:
                stack.append(stack[-1])
            elif s[idx] == ')':
                stack.pop()
            elif s[idx] == '-':
                stack.append(-1 * stack[-1])

            idx += 1

        return result

