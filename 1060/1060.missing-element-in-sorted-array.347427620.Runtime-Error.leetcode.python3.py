class solution:
    def missingElement(self, nums, k):
        index = 0
        for i in range(nums[0], nums[-1] + 1):
            if nums[index] == i:
                index += 1
            else:
                k -= 1
            if k == 0:
                return i
        while k:
            i += 1
            k -= 1
        return i

