class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res

