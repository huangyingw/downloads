class Solution(object):
    def pathSum(self, root, sum):
        paths = []
        self.preorder(root, sum - root.val, [root.val], paths)
        return paths

    def preorder(self, node, target, partial, paths):
        if not node:
            return
        if target == 0 and not node.left and not node.right:
            paths.append(partial)
        if node.left:
            self.preorder(node.left, target - node.left.val, partial + [node.left.val], paths)
        if node.right:
            self.preorder(node.right, target - node.right.val, partial + [node.right.val], paths)

