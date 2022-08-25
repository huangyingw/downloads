class Solution(object):
    def calculate(self, s):
        result, idx, num = 0, 0, 0
        stack = [1, 1]
        while idx < len(s):
            if s[idx].isdigit():
                num = num * 10 + ord(s[idx + 1]) - ord('0')
                if not s[idx + 1].isdigit():
                    result += stack.pop() * num
                idx += 1
                continue
            num = 0
            if s[idx] in ['(', '+']:
                stack.append(stack[-1])
            elif s[idx] == ')':
                stack.pop()
            elif s[idx] == '-':
                stack.append(-1 * stack[-1])
            idx += 1
        return result

