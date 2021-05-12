class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            current = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                current += [root.val]
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            result += [current]
        return result

