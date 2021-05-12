class Solution(object):
    def maxDepth(self, root):
        queue = [root]
        depth = 0
        while queue and root:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                print('node --> %s' % (node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

