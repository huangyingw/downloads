class Solution(object):
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            next_step = []
            for node in nodes:
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
            result += [node.val]
            nodes = next_step
        return result

