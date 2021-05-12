class Solution:
    def nextGreaterElement(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        nextGreat = {}
        nums3 = []
        res = []
        for num in nums2:
            while nums3 and nums3[-1] < num:
                nextGreat[nums3[-1]] = num
                nums3.pop()
            nums3.append(num)
        for num in nums1:
            if num in nextGreat:
                res.append(nextGreat[num])
            else:
                res.append(-1)
        return res

