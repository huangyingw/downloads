class Solution(object):
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leafInorder(root1) == self.leafInorder(root2)

    def leafInorder(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.leafInorder(root.left) + self.leafInorder(root.right)


class SolutionIterative:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)

    def getLeaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leaves

