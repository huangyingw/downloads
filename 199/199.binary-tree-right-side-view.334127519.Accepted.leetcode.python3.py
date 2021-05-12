class Solution(object):
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            next_step = []
            for node in queue:
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
            result += [node.val]
            queue = next_step
        return result

