class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def recursive(root, result):
            if not root:
                return
            recursive(root.left, result)
            recursive(root.right, result)
            result.append(root.val)
        recursive(root, result)
        return result

