class Solution(object):
    def bstToGst(self, root):
        self.bstToGst2(root, 0)
        return root

    def bstToGst2(self, root, SumNum):
        if root.right:
            SumNum = self.bstToGst2(root.right, SumNum)
        root.val += SumNum
        SumNum = root.val
        if root.left:
            SumNum = self.bstToGst2(root.left, SumNum)
        return SumNum

