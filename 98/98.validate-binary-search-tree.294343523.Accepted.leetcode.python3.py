class Solution(object):
    def isValidBST(self, root, minn=float('-inf'), maxx=float('inf')):
        if not root:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        return self.isValidBST(root.right, root.val, maxx) and self.isValidBST(root.left, minn, root.val)

