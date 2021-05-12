class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []

        while stack or root:
            if root.left:
                stack.append(root)
                root = root.left
            else:
                result.append(root.val)
                root = stack.pop()
                root = root.right
        return result

