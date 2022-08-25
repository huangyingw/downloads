class Solution(object):
    def maxDepth(self, root):
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

