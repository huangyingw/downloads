class Solution(object):
    def preorder(self, root):
        result = []
        if root == None:
            return result
        stack = [root]
        while len(stack) != 0:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result

