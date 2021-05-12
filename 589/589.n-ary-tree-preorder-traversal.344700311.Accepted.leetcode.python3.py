class Solution(object):
    def preorder(self, root):
        result = []
        stack = [root]
        while stack and root:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result

