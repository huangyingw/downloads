class Solution(object):
    def isSameTree(self, p, q):
        print('1 \n');
        if not p or not q:
            return p == q
        if p.val == q.val:
            return True
        print('2 \n');
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

