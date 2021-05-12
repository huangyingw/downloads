class Solution(object):
    def insertIntoBST(self, root, val):
        new_node = TreeNode(val)
        if not root:
            return new_node
        node = root
        while root:
            if val < node.val:
                if not node.left:
                    node.left = new_node
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = new_node
                    return root
                node = node.right

