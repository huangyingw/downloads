class Solution(object):
    def preorderTraversal(self, root):
        preorder = []
        stack = []
        while stack or root:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

