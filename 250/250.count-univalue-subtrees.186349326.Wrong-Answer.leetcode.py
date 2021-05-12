class Solution(object):
    def countUnivalSubtrees(self, root):
        if not root:
            return None

        left = self.countUnivalSubtrees(root.left)
        right = self.countUnivalSubtrees(root.right)

        if left == right:
            return root
        else:
            return None

