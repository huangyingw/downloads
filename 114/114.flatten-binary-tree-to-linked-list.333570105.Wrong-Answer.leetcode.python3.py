class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return
        if self.prev:
            self.prev.right = root
        savedRight = root.right
        root.right = root.left
        root.left = None
        self.flatten(root.right)
        self.flatten(savedRight)

