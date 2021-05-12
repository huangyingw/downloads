class Solution(object):
    def sortedListToBST(self, head):
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return self.list_to_bst([head], 0, count - 1)

    def list_to_bst(self, node_as_list, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left_subtree = self.list_to_bst(node_as_list, start, mid - 1)
        root = TreeNode(node_as_list[0].val)
        root.left = left_subtree
        node_as_list[0] = node_as_list[0].next
        root.right = self.list_to_bst(node_as_list, mid + 1, end)
        return root

