class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        inorder_indexes = {v: i for i, v in enumerate(inorder)}
        preorder_index = 1
        root = TreeNode(preorder[0])
        stack = [[root, 0, len(preorder) - 1]]
        while preorder_index < len(preorder):
            node, start, end = stack[-1]
            node_inorder_index = inorder_indexes[node.val]
            cur_val = preorder[preorder_index]
            cur_inorder_index = inorder_indexes[cur_val]
            if start <= cur_inorder_index <= end:
                new_node = TreeNode(cur_val)
                if cur_inorder_index < node_inorder_index:
                    node.left = new_node
                    stack.append([new_node, start, node_inorder_index - 1])
                else:
                    node.right = new_node
                    stack.append([new_node, node_inorder_index + 1, end])
                preorder_index += 1
            else:
                stack.pop()
        return root

