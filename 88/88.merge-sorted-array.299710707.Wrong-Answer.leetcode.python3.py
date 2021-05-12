class Solution:
    def merge(self, nums1, m, nums2, n):
        while m + n - 1 >= 0:
            if n < 0 or nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

