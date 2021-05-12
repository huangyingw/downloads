class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for parentheses in S:
            if parentheses == '(':
                stack.append('(')
            else:
                last_element = stack.pop()
                if last_element == '(':
                    stack.append(1)
                else:
                    stack.pop()
                    stack.append(last_element * 2)
            self.getSum(stack)
        return stack[0]

    def getSum(self, stack):
        if stack and stack[-1] == '(':
            return
        res = 0
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(res)

