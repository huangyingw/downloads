class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.max_sum = max(self.max_sum, root.val + left + right)
            return max(root.val + max(left, right), 0)
        dfs(root)
        return self.max_sum

