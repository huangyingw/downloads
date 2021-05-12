class Solution(object):
    def longestConsecutive(self, root):
        self.longest = 0
        self.consecutive(root, float('inf'), 0)
        return self.longest

    def consecutive(self, node, parent_val, sequence):
        if not node:
            return
        if node.val == 1 + parent_val:
            sequence += 1
        else:
            sequence = 1
        self.longest = max(self.longest, sequence)
        self.consecutive(node.left, node.val, sequence)
        self.consecutive(node.right, node.val, sequence)

