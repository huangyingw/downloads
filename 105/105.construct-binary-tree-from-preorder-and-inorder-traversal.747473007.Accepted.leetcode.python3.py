class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        self.index = 0

        def helper(start=0, end=len(inorder) - 1):
            if start > end:
                return
            root_val = preorder[self.index]
            inorder_index = find_index(root_val, start, end)
            if inorder_index == -1:
                return
            else:
                self.index += 1
            node = TreeNode(root_val)
            node.left = helper(start, inorder_index - 1)
            node.right = helper(inorder_index + 1, end)
            return node

        def find_index(root_val, start, end):
            for i in range(start, end + 1):
                if inorder[i] == root_val:
                    return i
            return -1
        return helper()

