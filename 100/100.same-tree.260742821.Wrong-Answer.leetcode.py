class Solution(object):
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        if p.val == q.val:
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

