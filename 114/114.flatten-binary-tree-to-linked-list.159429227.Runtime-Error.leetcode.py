class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return

        if self.prev:
            self.prev.right = root
            self.prev.left = None

        self.prev = root
        self.flatten(root.left)
        self.flatten(root.right)

