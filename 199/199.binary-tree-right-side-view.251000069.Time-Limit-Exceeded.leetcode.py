class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            for _ in range(len(queue)):
                if root.left:
                    queue += [root.left]
                if root.right:
                    queue += [root.right]
            result += [root.val]
        return result

