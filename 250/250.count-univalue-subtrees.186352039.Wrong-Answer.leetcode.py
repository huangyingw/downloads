class Solution(object):

    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root):
        self.isUnivalSubtrees(root)
        return self.count

    def isUnivalSubtrees(self, root):
        if not root:
            return None

        left = self.countUnivalSubtrees(root.left)
        right = self.countUnivalSubtrees(root.right)

        if left == right:
            self.count += 1
            return root
        else:
            return None

