class Solution(object):
    def longestConsecutive(self, root):
        def dfs(root, curLen):
            self.result = max(curLen, self.result)
            if root.left:
                if root.left.val == root.val + 1:
                    dfs(root.left, curLen + 1)
                else:
                    dfs(root.left, 1)
            if root.right:
                if root.right.val == root.val + 1:
                    dfs(root.right, curLen + 1)
                else:
                    dfs(root.right, 1)

        if not root:
            return 0

        self.result = 0
        dfs(root, 1)
        return self.result

