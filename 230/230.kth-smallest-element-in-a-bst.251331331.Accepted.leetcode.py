class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.helper(root)
        return self.result

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self.helper(node.right)

