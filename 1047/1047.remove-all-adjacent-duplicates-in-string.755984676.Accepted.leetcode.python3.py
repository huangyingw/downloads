class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        if not S:
            return ""
        for char in S:
            if not stack:
                stack.append(char)
            else:
                first = stack[-1]
                if first == char:
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return ""
        return ''.join(stack)

