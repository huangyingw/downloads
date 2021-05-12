class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if x == arr[mid]:
                left, right = mid, mid
                break
            elif x > arr[mid]:
                left = mid + 1
            else:
                right = mid
        else:
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                right = left
            else:
                left = right
        while right - left + 1 < k:
            if right + 1 == len(arr) or abs(arr[left - 1] - x) <= abs(arr[right + 1] - x):
                left -= 1
            else:
                right += 1
        return arr[left:right + 1]

