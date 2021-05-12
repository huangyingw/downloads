class Solution(object):
    def postorder(self, root):
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.children is not None:
                stack.extend(curr.children)
            res.append(curr.val)

