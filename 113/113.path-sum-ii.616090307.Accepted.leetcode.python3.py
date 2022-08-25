class Solution:
    def pathSum(self, root, sum):
        result = []
        stack = [(root, sum, [])]
        while stack:
            curr, target, partial = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right and target == curr.val:
                result.append(partial + [curr.val])
            stack.append((curr.right, target - curr.val, partial + [curr.val]))
            stack.append((curr.left, target - curr.val, partial + [curr.val]))
        return result

