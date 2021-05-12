class Solution(object):
    def rob(self, root):
        # res[0] means skip curr, res[1] means get curr
        res = self.rob_helper(root)
        return max(res[0], res[1])

    def rob_helper(self, root):
        if root is None:
            return [0, 0]
        left = self.rob_helper(root.left)
        right = self.rob_helper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res

