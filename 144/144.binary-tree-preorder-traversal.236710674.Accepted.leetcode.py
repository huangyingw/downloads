class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return result

