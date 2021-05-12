class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            current = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                current.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.insert(0, current)
        return result

