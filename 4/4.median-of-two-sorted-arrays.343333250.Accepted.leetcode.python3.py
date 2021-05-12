class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r, k = 0, n1, (n1 + n2 + 1) // 2
        print('l --> %s' % l)
        print('r --> %s' % r)
        while l < r:
            m1 = (l + r) // 2
            m2 = k - m1
            print('m1 --> %s' % m1)
            print('m2 - 1 --> %s' % str(m2 - 1))
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1, m2 = l, k - l
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1],
                 float('-inf') if m2 <= 0 else nums2[m2 - 1]
                 )
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(float('inf') if m1 >= n1 else nums1[m1],
                 float('inf') if m2 >= n2 else nums2[m2]
                 )
        return (c1 + c2) / 2

