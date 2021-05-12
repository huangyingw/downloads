class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return
        result = []

        def dfs(root):
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result

