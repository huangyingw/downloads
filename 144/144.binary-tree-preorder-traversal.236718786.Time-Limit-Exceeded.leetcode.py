class Solution(object):
    def preorderTraversal(self, root):
        result = []
        stack = [root]

        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = root.right

        return result

