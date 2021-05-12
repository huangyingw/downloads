class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = TreeNode(float('-inf'))
        self.first = None
        self.second = None

    def recoverTree(self, root: TreeNode) -> None:

        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        if self.prev.val > node.val:
            self.first = self.prev if not self.first else self.first
            self.second = node
        self.prev = node
        self.traverse(node.right)


class Solution1:
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

