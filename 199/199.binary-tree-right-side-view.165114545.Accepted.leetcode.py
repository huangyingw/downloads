class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            size = len(queue)

            for idx in range(size):
                root = queue.pop(0)

                if idx == 0:
                    result.append(root.val)

                if root.right:
                    queue.append(root.right)

                if root.left:
                    queue.append(root.left)

        return result

