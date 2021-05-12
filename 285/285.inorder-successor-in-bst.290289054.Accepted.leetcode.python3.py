class Solution(object):
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

