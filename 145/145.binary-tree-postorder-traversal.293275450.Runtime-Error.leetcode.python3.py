class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        result = deque()
        stack = [root]
        while stack:
            node = stack.pop()
            result.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(result)

