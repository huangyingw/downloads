class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                res.append(curr)
                continue
            stack.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res

