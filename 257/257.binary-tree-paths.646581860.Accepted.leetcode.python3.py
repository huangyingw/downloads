class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack = [(root, str(root.val))]
        result = []
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right:
                result.append(s)
            if node.right:
                stack.append((node.right, s + '->' + str(node.right.val)))
            if node.left:
                stack.append((node.left, s + '->' + str(node.left.val)))
        return result

