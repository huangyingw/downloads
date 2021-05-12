class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not isinstance(node, TreeNode):
                result.append(node)
                continue
            if node.right:
                stack.append(node.right)
            stack.append(node.val)
            if node.left:
                stack.append(node.left)
        return result

