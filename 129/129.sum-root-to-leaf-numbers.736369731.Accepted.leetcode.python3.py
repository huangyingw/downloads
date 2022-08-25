class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root, cur_sum=0):
            if not root:
                return 0

            if not root.left and not root.right:
                return cur_sum * 10 + root.val

            return dfs(root.left, cur_sum * 10 + root.val) + dfs(root.right, cur_sum * 10 + root.val)

        return dfs(root)


class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0

        def dfs(root, cur_sum=0):
            if not root:
                return

            cur_sum = cur_sum * 10 + root.val
            if not root.left and not root.right:
                self.sum += cur_sum
                return

            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)

        dfs(root)
        return self.sum

