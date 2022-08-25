class Solution(object):
    def insertIntoMaxTree(self, root, val):
        new_node = TreeNode(val)
        if not root:
            return new_node
        if root.val < val:
            new_node.left = root
            return new_node
        nrwwt = root
        start, prev = root.right, root
        while start:
            if(start.val > val):
                prev = start
                start = start.right
            else:
                break
        prev.right = new_node
        if not start:
            new_node.right = start
        else:
            new_node.left = start
        return root

