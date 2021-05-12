class Solution(object):
    def isValid(self, s):
        open_to_close = {'(': ')', '[': ']', '{': '}', }
        stack = []

        for char in s:
            if char in open_to_close:
                stack.append(char)
            elif not stack or open_to_close[stack.pop()] != char:
                return False

        return True

