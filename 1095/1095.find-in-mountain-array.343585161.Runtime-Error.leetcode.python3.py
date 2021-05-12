class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        mountain_arr.append(float('-inf'))
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid + 1) < mountain_arr.get(mid):
                right = mid
            else:
                left = mid + 1
        mountain = left
        left, right = 0, mountain + 1
        while left < right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                right = mid
            else:
                left = mid + 1
        left, right = mountain, n - 1
        while left < right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                left = mid + 1
            else:
                right = mid
        return -1

