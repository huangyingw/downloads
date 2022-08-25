class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        self.zigzagLevelOrder(root.left, 0, result, True)
        self.zigzagLevelOrder(root.right, 0, result, True)

    def zigzagLevelOrder(self, root, level, result=[], leftToRight=True):
        if leftToRight:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        self.zigzagLevelOrder(root.left, level + 1, result, not leftToRight)
        self.zigzagLevelOrder(root.right, level + 1, result, not leftToRight)

