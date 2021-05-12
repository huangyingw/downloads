class Solution(object):
    def sumNumbers(self, root):
        sum = 0

        def dfs(root, base):
            if not root.left and not root.right:
                sum += root.val + base
                return
            dfs(root.left, (base + root.val) * 10)
            dfs(root.right, (base + root.val) * 10)
        dfs(root, 0)
        return sum

