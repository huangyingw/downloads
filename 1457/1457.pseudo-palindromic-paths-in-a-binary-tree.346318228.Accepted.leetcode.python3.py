class Solution:
    count = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        map = [0] * 10

        self.dfs(root, map)
        return self.count

    def dfs(self, root, map):
        if not root:
            return

        map[root.val] += 1
        if not root.left and not root.right:
            self.count += self.isPalindrome(map)

        self.dfs(root.left, map)
        self.dfs(root.right, map)

        map[root.val] -= 1

    def isPalindrome(self, arr):
        flag = False
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                if flag:
                    return 0
                flag = True
        return 1

