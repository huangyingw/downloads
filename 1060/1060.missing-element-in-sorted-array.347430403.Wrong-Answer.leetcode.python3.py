class Solution(object):
    def missingElement(self, nums, k):
        nums.append(float("inf"))
        prev = nums[0]
        for num in nums[1:]:
            print('num --> %s' % num)
            missing = num - prev
            print('missing --> %s' % missing)
            k -= missing
            print('k --> %s' % k)
            if k <= 0:
                return num + 1
            prev = num
            print('prev --> %s' % prev)
            print()

