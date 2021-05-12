from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        freq1 = Counter(nums1)
        result = []
        for num in nums2:
            if num in freq1 and freq1[num] > 0:
                freq1[num] -= 1
                result.append(num)
        return result

