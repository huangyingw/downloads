class Solution(object):
    def closestValue(self, root, target):
        minDiff = sys.maxint
        result = root.val
        while root:
            diff = root.val - target
            if abs(diff) < minDiff:
                minDiff = abs(diff)
                result = root.val
            if diff < 0:
                root = root.right
            else:
                root = root.left
        return result

