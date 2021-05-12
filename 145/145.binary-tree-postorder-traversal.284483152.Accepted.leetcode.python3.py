

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)

