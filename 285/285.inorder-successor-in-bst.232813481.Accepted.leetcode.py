class Solution(object):
    def inorderSuccessor(self, root, p):
        if (not p) or (not root):
            return None

        if p.right:
            return self.leftmost(p.right)

        prev_root = None
        while root != p:
            if p.val <= root.val:
                prev_root = root
                root = root.left
            else:
                root = root.right

        return prev_root

    def leftmost(self, node):
        while node.left:
            node = node.left
        return node

