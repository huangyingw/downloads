class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        res = 0
        queue = [(root, root.val)]
        while queue:
            curr, curr_value = queue.pop(0)
            if not curr.left and not curr.right:
                res += curr_value
                continue
            if curr.left:
                queue.append((curr.left, curr_value * 10 + curr.left.val))
            if curr.right:
                queue.append((curr.right, curr_value * 10 + curr.right.val))
        return res

