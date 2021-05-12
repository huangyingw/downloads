class Solution:
    def closestValue(self, root, target):
        result = root.val
        while root:
            result = min((root.val, result), key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return result

