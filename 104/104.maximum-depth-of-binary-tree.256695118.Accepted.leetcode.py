class Solution(object):
    def maxDepth(self, root):
        queue = [root]
        depth = 0
        while queue and root:
            depth += 1
            for _ in range(len(queue)):
                root = queue.pop(0)
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
        return depth

