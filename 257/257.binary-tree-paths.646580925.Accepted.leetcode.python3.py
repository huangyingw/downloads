class Solution(object):
    def binaryTreePaths(self, root):
        def helper(node, partial):
            if not node:
                return
            partial.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(partial))
                return
            helper(node.left, partial[:])
            helper(node.right, partial)
        paths = []
        helper(root, [])
        return paths

