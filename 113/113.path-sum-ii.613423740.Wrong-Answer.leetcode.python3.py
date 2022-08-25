class Solution(object):
    def pathSum(self, root, sum):
        paths = []
        self.preorder(root, sum, [], paths)
        return paths

    def preorder(self, node, target, partial, paths):
        if not node:
            return
        print("node --> %s" % node.val)
        print("partial --> %s" % partial)
        if target == node.val and not node.left and not node.right:
            paths.append(partial)
        self.preorder(node.left, target - node.val, partial + [node.val], paths)
        self.preorder(node.right, target - node.val, partial + [node.val], paths)

