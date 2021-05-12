class Solution(object):
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            last = None
            for _ in range(len(queue)):
                root = queue.pop(0)
                if last:
                    last.next = root
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
                last = root
        return root

