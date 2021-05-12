class Solution:
    def getMinimumDifference(self, root):
        stack = [root]
        queue = []
        while stack and stack[0]:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
            else:
                queue.append(top.val)
                stack.pop(-1)
                if top.right:
                    stack.append(top.right)
                    top.right = None
        res = queue[-1] - queue[0]
        for i in range(1, len(queue)):
            res = min(res, queue[i] - queue[i - 1])
        return res

