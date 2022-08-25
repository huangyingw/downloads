class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == curr.val:
                res.append(ls + [curr.val])
            stack.append((root.left, sum - root.val, ls + [root.val]))
            stack.append((root.right, sum - root.val, ls + [root.val]))
        return res

