class Solution:
    def binaryTreePaths(self, root):
        paths = []
        self.get_path(paths, [], root)
        res = ['->'.join(p) for p in paths]
        return res

    def get_path(self, result, path, node):
        if not node.left and not node.right:
            result.append(path + [str(node.val)])
            return
        if node.left:
            self.get_path(result, path + [str(node.val)], node.left)
        if node.right:
            self.get_path(result, path + [str(node.val)], node.right)

