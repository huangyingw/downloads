class Solution(object):
    def rob(self, root):
        return max(self.helper(root))

    def helper(self, node):
        if not node:
            return 0, 0
        left_with, left_without = self.helper(node.left)
        right_with, right_without = self.helper(node.right)
        max_with = node.val + left_without + right_without
        max_without = max(left_with, left_without) + max(right_with, right_without)
        return max_with, max_without

