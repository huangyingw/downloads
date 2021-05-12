class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        sum = sum - root.val
        if sum == 0 and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return (left or right)

