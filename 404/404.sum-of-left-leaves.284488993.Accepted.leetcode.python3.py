class Solution(object):
    def sumOfLeftLeaves(self, root):
        stack = [root]
        res = 0
        while stack:
            curr = stack.pop(0)
            if curr:
                if curr.left:
                    if not curr.left.left and not curr.left.right:
                        res += curr.left.val
                stack.insert(0, curr.right)
                stack.insert(0, curr.left)
        return res

