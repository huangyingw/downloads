class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == "{":
                stack.append("}")
            elif i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            else:
                if not stack:
                    return False
                elif i != stack[-1]:
                    return False
                stack.pop()
        return not stack

