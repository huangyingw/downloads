class Solution(object):
    def upsideDownBinaryTree(self, root):
        node, parent, parentRight = root, None, None
        while node:
            left = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = left
        return parent

