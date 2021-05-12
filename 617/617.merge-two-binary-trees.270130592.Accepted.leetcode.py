class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left, t2.left)
            t.right = self.mergeTrees(t1.right, t2.right)
            return t
        else:
            return t1 or t2

