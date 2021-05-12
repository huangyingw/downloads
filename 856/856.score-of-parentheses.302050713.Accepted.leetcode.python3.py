class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last_element = stack.pop()
                stack[-1] += max(2 * last_element, 1)
        return stack.pop()

