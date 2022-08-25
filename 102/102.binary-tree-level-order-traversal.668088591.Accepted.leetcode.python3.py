class Solution(object):
    def levelOrder(self, root):
        queue = [root]
        result = []
        while queue and root:
            current = []
            size = len(queue)
            for _ in range(size):
                root = queue.pop(0)
                current += [root.val]
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            result += [current]
        return result

