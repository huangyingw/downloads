class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return depth

