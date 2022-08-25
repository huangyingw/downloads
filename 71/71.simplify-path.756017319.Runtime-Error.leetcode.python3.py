class Solution:
    def simplifyPath(self, path):
        stack = []
        for p in path.split('/'):
            if p == '..':
                stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)

