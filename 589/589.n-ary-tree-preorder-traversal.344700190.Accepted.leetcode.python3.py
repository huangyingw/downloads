class Solution(object):
    def preorder(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result

