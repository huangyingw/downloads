class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            print('depth --> %s' % (depth))
            for _ in range(len(queue)):
                node = queue.pop()
                print('node --> %s' % (node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

