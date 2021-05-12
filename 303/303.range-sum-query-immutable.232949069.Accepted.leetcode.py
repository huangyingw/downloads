class NumArray(object):
    def __init__(self, nums):
        self.ST = SegmentTree(nums)

    def sumRange(self, i, j):
        return self.ST.query(self.ST.root, i, j)


class Node(object):
    def __init__(self, start, end):
        self.left, self.right = None, None
        self.start, self.end, self.sum = start, end, 0


class SegmentTree(object):
    def __init__(self, vals):
        self.root = self.build(0, len(vals) - 1, vals)

    def build(self, start, end, vals):
        if start > end:
            return None
        root = Node(start, end)
        if start != end:
            mid = start + (end - start) / 2
            root.left = self.build(start, mid, vals)
            root.right = self.build(mid + 1, end, vals)
            root.sum = root.left.sum + root.right.sum
        else:
            root.sum = vals[start]
        return root

    def query(self, root, start, end):
        if not root or start > end:
            return 0
        if start <= root.start and end >= root.end:
            return root.sum
        mid = root.start + (root.end - root.start) / 2
        left_sum = right_sum = 0
        if start <= mid:
            if end > mid:
                left_sum = self.query(root.left, start, mid)
            else:
                left_sum = self.query(root.left, start, end)
        if end > mid:
            if start <= mid:
                right_sum = self.query(root.right, mid + 1, end)
            else:
                right_sum = self.query(root.right, start, end)
        return left_sum + right_sum

