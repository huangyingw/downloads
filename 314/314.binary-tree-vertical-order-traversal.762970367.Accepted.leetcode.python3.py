from collections import defaultdict


class Solution(object):
    def verticalOrder(self, root):
        vertical = defaultdict(list)
        frontier = [(root, 0)]
        for node, col in frontier:
            if node:
                vertical[col].append(node.val)
                frontier += [(node.left, col - 1), (node.right, col + 1)]
        return [vertical[col] for col in sorted(vertical)]

