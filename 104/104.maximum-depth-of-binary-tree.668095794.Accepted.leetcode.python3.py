class Solution(object):
    def maxDepth(self, root):
        queue = [root]
        depth = 0
        while queue and root:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

