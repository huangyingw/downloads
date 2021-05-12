class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

