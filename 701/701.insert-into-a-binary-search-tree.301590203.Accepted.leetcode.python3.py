class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

