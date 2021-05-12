class Solution(object):
    def pathSum(self, root, sum):
        paths = []
        self.preorder(root, sum, [], paths)
        return paths

    def preorder(self, node, target, partial, paths):
        if not node:
            return
        target -= node.val
        partial.append(node.val)
        if target == 0 and not node.left and not node.right:
            paths.append(partial[:])
        self.preorder(node.left, target, partial, paths)
        self.preorder(node.right, target, partial, paths)
        partial.pop()

