class Solution(object):
    def preorder(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return result

