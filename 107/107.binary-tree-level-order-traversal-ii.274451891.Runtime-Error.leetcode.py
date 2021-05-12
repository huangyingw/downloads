class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue, res = deque([(root, 1)]), []
        while queue:
            node, level = queue.popleft()
            if level > len(res):
                res = [[]] + res
            res[-level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res

