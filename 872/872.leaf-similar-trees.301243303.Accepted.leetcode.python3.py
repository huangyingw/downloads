class Solution:
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

