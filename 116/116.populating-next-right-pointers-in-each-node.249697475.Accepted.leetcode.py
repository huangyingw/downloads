class Solution(object):
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            last = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                if last:
                    last.next = node
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
                last = node
        return root

