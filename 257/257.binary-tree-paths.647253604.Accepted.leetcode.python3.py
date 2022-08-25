class Solution(object):
    def binaryTreePaths(self, root):
        def helper(node, partial):
            if not node:
                return
            if not node.left and not node.right:
                paths.append("->".join(partial + [str(node.val)]))
                return
            helper(node.left, partial + [str(node.val)])
            helper(node.right, partial + [str(node.val)])
        paths = []
        helper(root, [])
        return paths

