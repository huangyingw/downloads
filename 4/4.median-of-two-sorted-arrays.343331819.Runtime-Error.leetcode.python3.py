class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
        l, r, k = 0, n1, (n1 + n2 + 1) // 2
        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            print('m1 --> %s' % m1)
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1, m2 = l, k - l
        c1 = max(-sys.maxint - 1 if m1 <= 0 else nums1[m1 - 1],
                 -sys.maxint - 1 if m2 <= 0 else nums2[m2 - 1]
                 )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(sys.maxint if m1 >= n1 else nums1[m1],
                 sys.maxint if m2 >= n2 else nums2[m2]
                 )
        return (c1 + c2) // 2

