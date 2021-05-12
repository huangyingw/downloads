class NumArray(object):
    def __init__(self, nums):
        self.ls = len(nums)
        self.tree = [0] * (self.ls * 2)
        self.buildTree(nums)

    def buildTree(self, nums):
        i, j = self.ls, 0
        while i < 2 * self.ls:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        for i in reversed(range(1, self.ls)):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        i += self.ls
        self.tree[i] = val
        while i > 0:
            left = right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i / 2] = self.tree[left] + self.tree[right]
            i /= 2

    def sumRange(self, i, j):
        res = 0
        i += self.ls
        j += self.ls

        while i <= j:
            if i % 2 == 1:
                res += self.tree[i]
                i += 1
            if j % 2 == 0:
                res += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return res

