class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.mirrorVisit(root.left, root.right)

    def mirrorVisit(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
                return True
        return False

