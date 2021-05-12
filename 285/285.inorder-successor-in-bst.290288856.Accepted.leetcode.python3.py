class Solution(object):
    def inorderSuccessor(self, root, p):
        prev_root = None
        while root:
            if p.val < root.val:
                prev_root = root
                root = root.left
            else:
                root = root.right
        return prev_root

