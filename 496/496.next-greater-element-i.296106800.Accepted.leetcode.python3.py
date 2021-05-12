class Solution:
    def nextGreaterElement(self, nums1, nums2):
        l2 = len(nums2)
        nums2_next = [-1] * l2
        for i in range(l2 - 1):
            for j in range(i + 1, l2):
                if nums2[j] > nums2[i]:
                    nums2_next[i] = nums2[j]
                    break
        res = []
        for k in nums1:
            res.append(nums2_next[nums2.index(k)])
        return res

