class Solution(object):
    def binaryTreePaths(self, root):
        def helper(node, partial):
            if not node:
                return
            if not node.left and not node.right:
                paths.append("->".join(partial))
                return
            helper(node.left, partial.append(str(node.val)))
            helper(node.right, partial.append(str(node.val)))
        paths = []
        helper(root, [])
        return paths

