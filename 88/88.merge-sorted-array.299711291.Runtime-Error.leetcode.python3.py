class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        while m + n - 1 >= 0:
            if j < 0 or (i >= 0 and nums1[i] > nums2[j]):
                nums1[m + n - 1] = nums1[i]
                i -= 1
            else:
                nums1[m + n - 1] = nums2[j]
                j -= 1

