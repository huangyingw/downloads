class Solution(object):
    def levelOrder(self, root):
        queue = [root]
        result = []
        while queue and root:
            current = []
            for _ in queue:
                root = queue.pop(0)
                current += [root.val]
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            result += [current]
        return result

