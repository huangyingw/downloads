class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        lst = [root.val]
        for node in root.children:
            lst += self.preorder(node)
        return lst

