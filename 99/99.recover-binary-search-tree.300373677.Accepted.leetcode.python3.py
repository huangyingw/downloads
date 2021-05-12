class Solution:
    def __init__(self):
        self.previous = TreeNode(float('-inf'))
        self.first = None
        self.second = None

    def recoverTree(self, root):
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, node):
        curr = node
        while curr:
            if not curr.left:
                self.findMistake(curr)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == curr:
                    prev.right = None
                    self.findMistake(curr)
                    curr = curr.right
                else:
                    prev.right = curr
                    curr = curr.left

    def findMistake(self, node):
        if not self.first and self.previous.val >= node.val:
            self.first = self.previous
        if self.first and self.previous.val >= node.val:
            self.second = node
        self.previous = node

