class Solution(object):
    def pathSum(self, root, sum):
        paths = []
        self.preorder(root, sum, [], paths)
        return paths

    def preorder(self, node, target, partial, paths):
        if not node:
            return
        print("node --> %s" % node.val)
        print("target --> %s" % target)
        target -= node.val
        partial.append(node.val)
        if not node.left and not node.right and node.val == target:
            paths.append(partial)
        self.preorder(node.left, target, partial, paths)
        self.preorder(node.right, target, partial, paths)
        partial.pop()
        target += node.val

