class Solution(object):
    def inorderTraversal(self, root):
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        result = []
        dfs(root)
        return result

