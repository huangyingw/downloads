class Solution(object):
    def sumNumbers(self, root):
        def dfs(root, base):
            if not root.left and not root.right:
                return root.val + base
            dfs(root.left, (base + root.val) * 10)
            dfs(root.right, (base + root.val) * 10)
        return dfs(root, 0)

