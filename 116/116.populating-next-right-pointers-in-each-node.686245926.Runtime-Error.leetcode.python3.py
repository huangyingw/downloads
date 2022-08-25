class Solution(object):
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            last = None
            nex = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                if last:
                    last.next = node
                last = node
                if node.left:
                    nex += [node.left]
                if node.right:
                    nex += [node.right]
            queue = nex
        return root

