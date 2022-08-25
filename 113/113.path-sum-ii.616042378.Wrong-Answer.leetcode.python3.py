class Solution(object):
    def pathSum(self, root, sum):
        res = []
        if not root:
            return res
        if sum == root.val and not root.left and not root.right:
            return [[root.val]]
        left_res = self.pathSum(root.left, sum - root.val)
        right_res = self.pathSum(root.right, sum - root.val)
        return res

