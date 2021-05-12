class Solution(object):
    def inorderTraversal(self, root):
        result = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result

