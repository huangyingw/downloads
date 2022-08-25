class Solution(object):
    def connect(self, root):
        nodes = [root]
        while nodes and root:
            next_step = []
            last = None
            for node in nodes:
                if last:
                    last.next = node
                last = node
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
            nodes = next_step
        return root

