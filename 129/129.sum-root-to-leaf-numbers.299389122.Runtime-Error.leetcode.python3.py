class Solution:
    def sumNumbers(self, root, summ=0):
        if not root:
            return 0
        if not root.left and not root.right:
            return summ * 10 + root.val
        return self.getSum(root.left, summ * 10 + root.val) + self.getSum(root.right, summ * 10 + root.val)

