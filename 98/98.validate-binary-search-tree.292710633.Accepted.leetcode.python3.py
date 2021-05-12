class Solution(object):
    def isValidBST(self, root):
        self.correct = True
        self.prev = float('-inf')
        self.inorder(root)
        return self.correct

    def inorder(self, node):
        if not node or not self.correct:
            return
        self.inorder(node.left)
        if node.val <= self.prev:
            self.correct = False
            return
        self.prev = node.val
        self.inorder(node.right)

