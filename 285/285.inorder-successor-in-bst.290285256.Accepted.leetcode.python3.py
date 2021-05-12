class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succ = root
                root = root.left
        return succ

