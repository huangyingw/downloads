class Solution(object):
    def closestValue(self, root, target):
        gap = abs(root.val - target)
        ans = root
        while root is not None:
            if root.val == target:
                return root.val
            elif target < root.val:
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.left
            else:
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.right
        return ans.val

