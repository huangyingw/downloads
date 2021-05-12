class Solution(object):
    def hasPathSum(self, root, sum):
        print("sum --> %s" % sum)
        print("root --> %s" % 'N' if not root else root.val)
        if not root or root.val > sum:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

