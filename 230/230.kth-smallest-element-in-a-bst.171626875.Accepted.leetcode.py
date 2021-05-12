class Solution(object):
    count = 0
    result = -1

    def kthSmallest(self, root, k):
        def dfs(root, k):
            if not root or self.count > k:
                return

            dfs(root.left, k)
            self.count += 1

            if self.count == k:
                self.result = root.val

            dfs(root.right, k)

        dfs(root, k)
        return self.result

