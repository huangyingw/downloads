class Solution(object):
    def countUnivalSubtrees(self, root):
        if not root:
            return 0

        sumV = []
        sumV.append(0)
        self.dfs(root, sumV)
        return sumV[0]

    def dfs(self, root, sumV):
        if not root:
            return True

        left = self.dfs(root.left, sumV)
        right = self.dfs(root.right, sumV)

        if (left and right and (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val)):
            sumV.set(0, sumV.get(0) + 1)
            return True

        return False

