class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        queue = [root]
        while len(queue):
            curr = queue.pop(0)
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root

