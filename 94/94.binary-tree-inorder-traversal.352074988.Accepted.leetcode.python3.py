class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                result.append(curr)
                continue
            if curr.right:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left:
                stack.append(curr.left)
        return result

