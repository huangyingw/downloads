class Solution(object):
    def sumOfLeftLeaves(self, root):
        sum = 0
        if root != None:
            if root.left != None:
                if root.left.left == None and root.left.right == None:
                    sum += root.left.val
                else:
                    sum += self.sumOfLeftLeaves(root.left)
            if root.right != None:
                sum += self.sumOfLeftLeaves(root.right)
        return sum

