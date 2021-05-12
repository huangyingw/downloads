class Solution(object):
    def preorder(self, root):
        result = []
        stack = []
        while stack or root:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result

