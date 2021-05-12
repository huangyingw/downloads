class Solution(object):
    def postorder(self, root):
        if root == None:
            return []
        lst = [root.val]
        for node in root.children[::-1]:
            lst = self.postorder(node) + lst
        return lst

