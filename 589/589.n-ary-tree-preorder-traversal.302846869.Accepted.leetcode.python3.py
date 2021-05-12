class Solution(object):
    def preorder(self, root):
        if root == None:
            return []
        lst = [root.val]
        for node in root.children:
            lst += self.preorder(node)
        return lst

