class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            if curr.right:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left:
                stack.append(curr.left)
        return res

