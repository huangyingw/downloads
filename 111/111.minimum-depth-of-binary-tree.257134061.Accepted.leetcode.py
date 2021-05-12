class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth, rightMost = 1, root
        while queue:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node == rightMost:
                depth += 1
                if node.right:
                    rightMost = node.right
                else:
                    rightMost = node.left
        return depth

