class Solution(object):
    def connect(self, root):
        if not root:
            return
        nodes = [root]
        while nodes:
            next_step = []
            last = None
            for node in nodes:
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
                last.next = node
                last = node
            nodes = next_step
        return root

