class Solution(object):
    def bstToGst(self, root):
        self.running_sum = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            node.val += self.running_sum
            self.running_sum = node.val
            inorder(node.left)
        inorder(root)
        return root

