class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

