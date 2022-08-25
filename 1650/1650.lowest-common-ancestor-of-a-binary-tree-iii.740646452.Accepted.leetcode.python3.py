class Solution:
    def lowestCommonAncestor(self, a, b):
        ancestors = set()
        while a:
            ancestors.add(a)
            a = a.parent
        while b:
            if b in ancestors:
                return b
            b = b.parent

