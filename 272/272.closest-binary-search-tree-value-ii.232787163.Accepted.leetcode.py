class Solution(object):
    def closestKValues(self, root, target, k):
        stk1 = []
        stk2 = []
        self.inorder(root, False, target, stk1)
        self.inorder(root, True, target, stk2)

        res = []
        for _ in xrange(k):
            if not stk1:
                res.append(stk2.pop())
            elif not stk2:
                res.append(stk1.pop())
            else:
                if abs(stk1[len(stk1) - 1] - target) < abs(stk2[len(stk2) - 1] - target):
                    res.append(stk1.pop())
                else:
                    res.append(stk2.pop())
        return res

    def inorder(self, root, reverse, target, stk):
        if root is None:
            return
        self.inorder(root.right, reverse, target, stk) if reverse else self.inorder(root.left, reverse, target, stk)
        # The first inequality is less than or equal, the second inequality must be larger than (without equal).
        # Or the first is less than, the second is larger than or equal to
        if not reverse and target <= root.val:
            return
        if reverse and target > root.val:
            return
        stk.append(root.val)
        self.inorder(root.left, reverse, target, stk) if reverse else self.inorder(root.right, reverse, target, stk)

