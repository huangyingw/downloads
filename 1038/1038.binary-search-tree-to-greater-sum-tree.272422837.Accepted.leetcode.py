class Solution(object):
    ListNode = []

    def bstToGst(self, root):
        self.ListNode = []
        self.dfs(root)
        SumNum = 0
        for node in self.ListNode:
            SumNum += node.val
            node.val = SumNum
        return root

    def dfs(self, node):
        if node:
            if node.right:
                self.dfs(node.right)
            self.ListNode.append(node)
            if node.left:
                self.dfs(node.left)

