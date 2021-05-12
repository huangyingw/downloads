class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.diameter = max(self.diameter, l + r)
            return max(l, r) + 1
        depth(root)
        return self.diameter

