class Solution(object):
    def flatten(self, root):
        if not root:
            return
        current = root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if current != node:
                current.right = node
                current.left = None
                current = node

