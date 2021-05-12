class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ret = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ret.add(nums1[i])
                i += 1
                j += 1
        return list(ret)

