class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        stack = [(root, sum - root.val, [])]
        while stack:
            curr, target, partial = stack.pop()
            if not curr:
                continue
            print("curr --> %s" % curr.val)
            print("target --> %s" % target)
            print("partial --> %s" % partial)
            if not curr.left and not curr.right and target == curr.val:
                result.append(partial + [curr.val])
            stack.append((curr.right, target - curr.val, partial + [curr.val]))
            stack.append((curr.left, target - curr.val, partial + [curr.val]))
        return result

