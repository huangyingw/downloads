class Solution(object):
    def flatten(self, root):
        current = root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if current != node:
                current.right = node
                current.left = None
                current = node

