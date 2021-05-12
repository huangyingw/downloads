class Solution(object):
    def isSameTree(self, p, q):
        print('1 \n');
        print('2 \n');
        print('3 \n');
        if not p or not q:
            return p == q
        if p.val == q.val:
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

