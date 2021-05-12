class Solution(object):
    def recoverTree(self, root):
        self.swapped1 = None
        self.swapped2 = None
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)
        self.swapped1.val, self.swapped2.val = self.swapped2.val, self.swapped1.val

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if node.val <= self.prev.val:
            if not self.swapped1:
                self.swapped1 = self.prev
            if self.swapped1:
                self.swapped2 = node
        self.prev = node
        self.inorder(node.right)

