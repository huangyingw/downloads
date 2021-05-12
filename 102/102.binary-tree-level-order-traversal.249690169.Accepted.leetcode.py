class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        this_level = [root]
        while this_level:
            result += [[node.val for node in this_level]]
            this_level = [child for node in this_level for child in (node.left, node.right) if child]
        return result

