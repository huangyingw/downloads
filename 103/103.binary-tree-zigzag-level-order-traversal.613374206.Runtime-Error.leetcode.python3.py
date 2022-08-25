class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        zigzagLevelOrder(root.left, 0, result, True)
        zigzagLevelOrder(root.right, 0, result, True)

    def zigzagLevelOrder(root, level, result=[], leftToRight=True):
        if leftToRight:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        zigzagLevelOrder(root.left, level + 1, result, not leftToRight)
        zigzagLevelOrder(root.right, level + 1, result, not leftToRight)

