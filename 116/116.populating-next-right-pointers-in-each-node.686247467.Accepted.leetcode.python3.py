class Solution(object):
    def connect(self, root):
        nodes = [root]
        while root and nodes:
            next_step = []
            last = None
            for node in nodes:
                if last:
                    last.next = node
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
                last = node
            nodes = next_step
        return root

