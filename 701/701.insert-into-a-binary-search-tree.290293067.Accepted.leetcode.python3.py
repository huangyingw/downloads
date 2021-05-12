class Solution():
    def insertIntoBST(self, root, val):
        root_head = root
        root_val = TreeNode(val)
        while(True):
            if val < root.val:
                if root.left != None:
                    root = root.left
                else:
                    root.left = root_val
                    break
            else:
                if root.right != None:
                    root = root.right
                else:
                    root.right = root_val
                    break
        return root_head

