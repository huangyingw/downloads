class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

