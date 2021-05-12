class Solution(object):
    def levelOrderBottom(self, root):
        traversal = []
        self.inorder(root, 0, traversal)
        return traversal[::-1]

    def inorder(self, node, depth, traversal):
        if not node:
            return
        if len(traversal) == depth:
            traversal.append([])
        self.inorder(node.left, depth + 1, traversal)
        traversal[depth].append(node.val)
        self.inorder(node.right, depth + 1, traversal)

