class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return

        if self.prev:
            self.prev.right = root
            self.prev.left = None

        savedRight = root.right
        self.prev = root
        self.flatten(root.right)
        self.flatten(savedRight)

