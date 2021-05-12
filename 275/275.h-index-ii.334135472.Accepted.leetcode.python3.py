class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - left

