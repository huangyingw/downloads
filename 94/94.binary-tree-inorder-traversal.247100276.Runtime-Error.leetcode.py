class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = [root]
        while stack:
            if root.left:
                stack += [root]
                root = root.left
            else:
                root = stack.pop()
                result += [root]
                root = root.right
        return result

