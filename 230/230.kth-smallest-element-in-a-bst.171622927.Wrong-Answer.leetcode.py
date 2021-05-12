class Solution(object):
    count = 0

    def kthSmallest(self, root, k):
        if not root:
            return

        self.kthSmallest(root.left, k)
        self.count += 1
        print('count --> %s' % self.count)
        print('root --> %s' % root.val)

        if self.count == k:
            return root.val

        self.kthSmallest(root.right, k)

