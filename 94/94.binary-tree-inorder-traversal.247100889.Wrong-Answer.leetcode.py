class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = [root]
        while stack and root:
            if root.left:
                stack += [root]
                root = root.left
            else:
                root = stack.pop()
                result += [root]
                root = root.right
        return result

