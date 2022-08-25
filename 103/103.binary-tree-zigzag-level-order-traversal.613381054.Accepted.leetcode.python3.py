class Solution(object):
    def dfs(self, root, level, result=[], leftToRight=True):
        if not root:
            return
        if level == len(result):
            result.append([])
        if leftToRight:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        self.dfs(root.left, level + 1, result, not leftToRight)
        self.dfs(root.right, level + 1, result, not leftToRight)

    def zigzagLevelOrder(self, root):
        result = []
        self.dfs(root, 0, result, True)
        return result

