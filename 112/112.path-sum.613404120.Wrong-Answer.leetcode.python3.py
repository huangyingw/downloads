class Solution(object):
    def hasPathSum(self, root, sum):
        def dfs(root, sum):
            if not root:
                return sum == 0
            return dfs(root.left, sum - root.val) or dfs(root.right, sum - root.val)
        if not root:
            return False
        return dfs(root, sum)

