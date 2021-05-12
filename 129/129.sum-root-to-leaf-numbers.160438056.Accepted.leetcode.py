class Solution(object):
    def sumNumbers(self, root):
        self.sum = 0

        def dfs(root, base):
            if not root:
                return

            if not root.left and not root.right:
                self.sum += root.val + base
                return
            dfs(root.left, (base + root.val) * 10)
            dfs(root.right, (base + root.val) * 10)
        dfs(root, 0)
        return self.sum

