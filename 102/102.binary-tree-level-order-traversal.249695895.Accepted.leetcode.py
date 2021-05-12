class Solution(object):
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            next_step = []
            result += [[]]
            for node in nodes:
                result[-1] += [node.val]
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
            nodes = next_step
        return result

