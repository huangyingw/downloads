class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        self.index = 0

        def helper(order):
            if not order:
                return
            root_val = preorder[self.index]
            inorder_index = find_index(order, root_val)
            if inorder_index == -1:
                return
            else:
                self.index += 1
            node = TreeNode(root_val)
            node.left = helper(order[:inorder_index])
            node.right = helper(order[inorder_index + 1:])
            return node

        def find_index(arr, val):
            for i in range(len(arr)):
                if arr[i] == val:
                    return i
            return -1
        return helper(inorder)

