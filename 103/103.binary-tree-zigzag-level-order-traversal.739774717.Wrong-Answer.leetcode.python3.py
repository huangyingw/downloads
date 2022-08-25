class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        leftToRight = True
        while queue:
            current = []
            size = len(queue)
            for _ in range(size):
                root = queue.pop(0)
                if leftToRight:
                    current.append(root.val)
                else:
                    current.insert(0, root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(current)
        return result

