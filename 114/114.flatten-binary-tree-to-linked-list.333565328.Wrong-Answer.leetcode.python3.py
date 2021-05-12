class Solution(object):
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if not root.left:
            return None
        it = root
        while it.right:
            it = it.right
        it.right = root.right
        root.right = root.left
        root.left = None

