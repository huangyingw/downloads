class Solution(object):
    def isSymmetric(self, root, left=None, right=None):
        if not root:
            return True
        if not left and not right:
            print('root --> %s' % (root.val if root else 'None'))
            print('left --> %s' % (left.val if left else 'None'))
            print('right --> %s' % (right.val if right else 'None'))
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isSymmetric(root, left.left, right.right) and self.isSymmetric(root, left.right, right.left)

