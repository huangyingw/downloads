class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = [(root, 0)]
        levelMap = {}

        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

            if level in levelMap:
                levelMap[level].append(node.val)
            else:
                levelMap[level] = [node.val]

        result = []
        spiral = False
        for key, value in levelMap.iteritems():
            if spiral:
                value = value[::-1]
            result.append(value)
            spiral = not spiral
        return result

