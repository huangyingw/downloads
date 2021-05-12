class Solution(object):
    def longestConsecutive(self, root):
        def consecutive(root):
            if root == None:
                return 0
            else:
                left, right = 0, 0
                if root.left:
                    if root.left.val == root.val + 1:
                        left = 1 + consecutive(root.left)
                if root.right:
                    if root.right.val == root.val + 1:
                        right = 1 + consecutive(root.right)
                return max(left, right, 1)

        def dfs(root):
            s = []
            s.append(root)
            while s:
                root = s.pop()
                res.append(consecutive(root))
                if root.left:
                    s.append(root.left)
                if root.right:
                    s.append(root.right)
        if not root:
            return 0

        res = []
        dfs(root)
        return max(res)

