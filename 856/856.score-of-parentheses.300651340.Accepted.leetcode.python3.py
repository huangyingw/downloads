class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = bal = 0
        for i in range(len(S)):
            bal += 1 if S[i] == '(' else -1
            if S[i] == ')' and S[i - 1] == '(':
                res += 2**bal
        return res


class Solution1:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last_element = stack.pop()
                stack[-1] += max(2 * last_element, 1)
        return stack.pop()


class Solution2:
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

