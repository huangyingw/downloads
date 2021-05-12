class Solution(object):
    def sortedListToBST(self, head):
        size = 0
        self.current = head

        while head:
            size += 1
            head = head.next

        def dfs(start, end):
            if start > end:
                return None

            mid = (start + end) / 2
            root = TreeNode(0)
            root.left = dfs(start, mid - 1)
            root.val = self.current.val
            self.current = self.current.next
            root.right = dfs(mid + 1, end)
            return root

        return dfs(0, size - 1)

