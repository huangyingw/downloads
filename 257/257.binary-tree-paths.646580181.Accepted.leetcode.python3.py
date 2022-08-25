class Solution(object):
    def binaryTreePaths(self, root):
        paths = []

        def dfs(root, curr):
            if not root.left and not root.right:
                paths.append(curr + str(root.val))
                return
            if root.left:
                dfs(root.left, curr + str(root.val) + '->')
            if root.right:
                dfs(root.right, curr + str(root.val) + '->')
        curr = ""
        dfs(root, curr)
        return paths

