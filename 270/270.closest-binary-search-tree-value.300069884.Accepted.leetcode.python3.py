class Solution:
    def closestValue(self, root, target):
        child = root.left if root.val > target else root.right
        if not child:
            return root.val
        child_val = self.closestValue(child, target)
        return min((root.val, child_val), key=lambda x: abs(x - target))

