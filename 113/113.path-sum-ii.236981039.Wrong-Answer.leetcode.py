class Solution(object):
    def pathSum(self, root, sum):
        result = []

        def dfs(root, curr_sum, sum, path, result):
            if not root:
                return

            curr_sum += root.val
            if curr_sum == sum and not root.left and not root.right:
                result.append(path + [root.val])
                return

            if root.right:
                dfs(root.right, curr_sum, sum, path + [root.val], result)

        dfs(root, 0, sum, [], result)
        return result

