class Solution(object):
    def maxDepth(self, root):
        q, level = root and [root], 0
        while q:
            q, level = [child for node in q for child in node.children if child], level + 1
        return level

