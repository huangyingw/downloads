class Solution:
    def isSubtree(self, s, t):
        if not s:
            return s is t
        if self.isEqual(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isEqual(self, m, n):
        if not m or not n:
            return m is n
        return m.val == n.val and self.isEqual(m.left, n.left) and self.isEqual(m.right, n.right)

