class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            self.intersect(nums2, nums1)
        d = {}
        res = []
        for no in nums1:
            d[no] = d.get(no, 0) + 1
        for no in nums2:
            if no in d and d[no]:
                res.append(no)
                d[no] -= 1
        return res

