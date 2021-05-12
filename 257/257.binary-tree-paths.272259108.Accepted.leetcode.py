class Solution:
    def binaryTreePaths(self, r):
        stack = []
        res = []

        def dfs(root):
            if not root:
                return []
            stack.append(root.val)
            if not root.left and not root.right:
                res.append('->'.join(str(v) for v in stack))
            dfs(root.left)
            dfs(root.right)
            stack.pop()
        dfs(r)
        return res

