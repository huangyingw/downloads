class Solution(object):
    def pathSum(self, root, sum):
        paths = []
        self.preorder(root, sum, [], paths)
        return paths

    def preorder(self, node, target, partial, paths):
        print("partial --> %s" % partial)
        if not node:
            return
        print("node --> %s" % node.val)
        if target == node.val and not node.left and not node.right:
            paths.append(partial)
        self.preorder(node.left, target - node.val, partial + [node.val], paths)
        self.preorder(node.right, target - node.val, partial + [node.val], paths)

