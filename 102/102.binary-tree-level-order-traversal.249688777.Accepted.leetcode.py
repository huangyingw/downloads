class Solution(object):
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        level_nodes = [root]
        while level_nodes:
            new_level_nodes = []
            result += [[]]
            for node in level_nodes:
                result[-1] += [node.val]
                if node.left:
                    new_level_nodes += [node.left]
                if node.right:
                    new_level_nodes += [node.right]
            level_nodes = new_level_nodes
        return result

