class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
        return depth

