class Solution:
    def rangeSumBST(self, root, L, R):
        self.ans = 0

        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        dfs(root)
        return self.ans

