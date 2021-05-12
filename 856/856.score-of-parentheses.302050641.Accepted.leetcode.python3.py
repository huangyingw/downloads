class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = bal = 0
        for i in range(len(S)):
            bal += 1 if S[i] == '(' else -1
            if S[i] == ')' and S[i - 1] == '(':
                res += 2**bal
        return res

