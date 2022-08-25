class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        self.dfs(root, sum)
        return self.ans

    def dfs(self, root, sum, arr=[], cur_sum=0):
        if not root:
            return cur_sum

        cur_sum += root.val
        arr.append(root.val)

        if not root.left and not root.right and cur_sum == sum:
            self.ans.append([num for num in arr])

        self.dfs(root.left, sum, arr, cur_sum)
        self.dfs(root.right, sum, arr, cur_sum)

        arr.pop()

